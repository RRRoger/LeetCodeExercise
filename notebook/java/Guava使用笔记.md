# Guava 使用最佳实践

参考链接：https://www.kancloud.cn/wizardforcel/java-opensource-doc/112616

```xml
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>31.0.1-jre</version>
</dependency>
```

## 字符串的比较

>   当一个对象中的字段可以为null时，实现equals方法会很痛苦，因为不得不分别对它们进行null检查
>
>   使用**Objects.equal**可以有效避免抛出*NullPointerException*

```java
Objects.equal(null, null);
Objects.equal("", null);
Objects.equal("A", "B");
```

## 新建集合 new Collections

>   减少钻石符号("<>")的使用

### List

```java
List<Object> list = Lists.newArrayList(null, "", "a", 19);
```

### Map

```java
Map<String, Object> map = Maps.newHashMap();
map.put("k1", "v1");
map.put("k2", "v2");
map.put("k3", 1000);
```

### List分组

```java
List<List<Object>> partitions = Lists.partition(list, 3);
System.out.println("partitions:" + partitions);

for (List<Object> each : partitions) {
    // do something
    System.out.println("each: " + each);
}
```

## Ints

```
其他Floats,Longs,Doubles类似
```

```java
// 创建int List
List<Integer> integers = Ints.asList(1, 2, 3, 4, 5);

// 最大最小值
Ints.min(1, 2, 3, 4, 5, 5, 5, 5, 5);

// 包含
int[] arr1 = {1, 2, 3, 4, 5, 5, 5, 5, 5};
System.out.println(Ints.contains(arr1 , 5));

//...
```

## 字符串连接

>   更加灵活

```java
private static final Joiner joiner = Joiner.on(",").skipNulls();
private static final Joiner joiner1 = Joiner.on(",").useForNull("_DEFAULT_");

List<String> list = Lists.newArrayList(null, "A", "B", "C", "D", "E", "F");

// 忽略空值报错
String x = joiner.join(list);
System.out.println("x: " + x);

// 替换空值
String y = joiner1.join(list);
System.out.println("y: " + y);
```

## 字符串分割

>   更加灵活

```java
private static final Splitter splitter = Splitter.on(",");

// 忽略空值
private static final Splitter splitter1 = Splitter.on(",").omitEmptyStrings();

String x = "1,1,1,1,1,,,,";
Iterable<String> iterable = splitter.split(x);
Iterable<String> iterable1 = splitter1.split(x);
System.out.println("iterable: " + iterable);
System.out.println("iterable1: " + (iterable1));

// 转成list
List<String> list = splitter.splitToList(x);
System.out.println("list: " + list);
```

## 字符集转化

>   使用**getBytes(Charsets.UTF_8)**而不是**string.getBytes("UTF-8")**

```java
byte[] bytes = "abc".getBytes(Charsets.UTF_8);
for (byte b : bytes) {
    System.out.println(b);
}
```

## 驼峰 <-> 下划线

```java
// 下划线转驼峰
// 首字母小写
System.out.println(CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.LOWER_CAMEL, "student_name"));
// 首字母大写
System.out.println(CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.UPPER_CAMEL, "student_name"));

// 驼峰转下划线
System.out.println(CaseFormat.LOWER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, "studentName"));
```

## 简化抛异常

```java
// 值为空就抛异常
Preconditions.checkNotNull(null, "数据不能为null");

// 表达式值为假就抛异常
Preconditions.checkArgument(a > b, "表达式值为假!");
```

## 不可变集合

```java
// Immutable: 永恒的
// 不希望被改变; 快; 安全;
// 优于jdk原生的 unmodifiableList
ImmutableList<String> colors = ImmutableList.of(
        "red",
        "yellow",
        "blue",
        "green",
        "black");

System.out.println("colors: " + colors);
System.out.println(mapper.writeValueAsString(colors));
```

## HashMultiset

```java
HashMultiset<String> multiset = HashMultiset.create();
multiset.add("a");
multiset.add("b");
multiset.add("c");
multiset.add("a"); // 有两个a
System.out.println("multiset: " + multiset); // multiset: [a x 2, b, c]
System.out.println("multiset.entrySet: " + multiset.entrySet()); // multiset: [a x 2, b, c]
System.out.println("multiset.elementSet: " + multiset.elementSet()); // multiset: [a, b, c]

Set<Multiset.Entry<String>> entries = multiset.entrySet();
for (Multiset.Entry<String> entriy : entries) {
    System.out.println("元素: " + entriy.getElement() + ", 个数: " + entriy.getCount());
}
```

## hashMultimapTest

```java
Multimap<String, String> multimap = HashMultimap.create();
multimap.put("a", "1");
multimap.put("a", "2");
multimap.put("a", "3");
multimap.put("b", "1");
multimap.put("b", "2");
multimap.put("c", "1");
Collection<String> aValues = multimap.get("a");
System.out.println(aValues);
System.out.println(multimap.containsEntry("a", "1"));
System.out.println(multimap.containsEntry("a", "4"));

Map<String, Collection<String>> jdkMap = multimap.asMap();
for (Collection<String> col : jdkMap.values()) {
    System.out.println("col: " + col);
    System.out.println("col.getClass(): " + col.getClass());
}
System.out.println("jdkMap: " + jdkMap);
```