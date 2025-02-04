![image](https://github.com/user-attachments/assets/f4bb4bd8-bfd8-4e0e-a633-fa5d7b75e404)# hunk_classification:
```
Changeing Identifiers: 
  Replacing Identifiers: Changing the name of an identifier.
  Adding Identifiers: Adding a new identifier to the code.
  Removing Identifiers: Removing an identifier (such as a variable, method, class, or constant) that is no longer needed or used in the code.
  Changing Identifier Type: modifying the data type of an identifier

Replacing Code: Replacing the logic of existing code.
Removing Code: Deleting unnecessary code.
Adding Code: Inserting new code into the existing structure.
Changing Return Type: Modifying the return type of a method.
Changing Access Modifier: Adjusting the visibility of a class, method, or field to control access (e.g., from `private` to `public`).
  Changing Method Access Modifier
  Changing Attribute Access Modifier
  Changing Class Access Modifier

Changing Modifier: refers to any operation that adds or removes a modifier (e.g., final, static, abstract, synchronized, etc.) to or from a code element, such as methods, attributes, variables, parameters, or classes.
  Adding Method Modifier (final, static, abstract, synchronized)
  Replacing Method Modifier
  Removing Method Modifier (final, static, abstract, synchronized)
  Adding Attribute Modifier (final, static, transient, volatile)
  Removing Attribute Modifier (final, static, transient, volatile)
  Replacing Attribute Modifier (final, static, transient, volatile)
  Adding Variable Modifier (final)
  Adding Parameter Modifier (final)
  Removing Variable Modifier (final)
  Removing Parameter Modifier (final)
  Replacing Variable Modifier (final)
  Replacing Parameter Modifier (final)
  Adding Class Modifier (final, static, abstract)
  Removing Class Modifier (final, static, abstract)
  Replacing Class Modifier (final, static, abstract)

Changing Annotation:
  Adding Method Annotation
  Removing Method Annotation
  Replacing Method Annotation
  Adding Attribute Annotation
  Removing Attribute Annotation
  Replacing Attribute Annotation
  Adding Class Annotation
  Removing Class Annotation
  Replacing Class Annotation
  Adding Parameter Annotation
  Removing Parameter Annotation
  Replacing Parameter Annotation
  Adding Variable Annotation
  Removing Variable Annotation
  Replacing Variable Annotation

Changing Comments: Modifying the comments in the code, typically to improve documentation, correct the content, or update the description.
  Adding Comments
  Removing Comments
  Replacing Comments

Exception Handling
Adding Thrown Exception Type
Removing Thrown Exception Type
Changing Thrown Exception Type


Extracting Variable
Inlining Variable


Reordering Code
```


# file_classification:
```
file created -> new entity in the code
file removed -> entity removed from the code
file renamed -> entity changed name, file was modified
file modified -> file was modified
```

# 不同位置不同文件，修改内容相似
```
cc6cc217cc14dedd2767c686bb91b064213f2f75
636ca09e9ed091efabc7784661e8f0994175c73d
636ca09e9ed091efabc7784661e8f0994175c73d
```

# 不算Adding an Identifier
```
@@ -146,6 +146,8 @@ handlerConfig	VARIABLENAME
 ,	METHODINVOCATIONCOMMA
 getFilter	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
+handler	VARIABLENAME
+,	METHODINVOCATIONCOMMA
 handlerConfig	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ,	METHODINVOCATIONCOMMA
```
在这种情况下，这并不算 **"Adding an Identifier"**，而是 **方法调用时添加参数**。

### 解释：
- **"Adding an Identifier"** 一般是指在代码中新增一个变量、函数名或类型等标识符（例如变量声明、函数定义、类名等）。例如：

```java
int newVariable;  // Adding an identifier: new variable
```

而你提供的代码：

```java
getFilter(handler, handlerConfig);
```

是对已定义的 `getFilter` 方法的调用，并且 **在调用时新增了参数**（`handler` 和 `handlerConfig`）。这只是调用了一个已有的方法，而不是声明新的标识符。因此，它不算 "Adding an Identifier"。

### 总结：
- **"Adding an Identifier"** 通常指的是在代码中添加新的变量、方法、类型等标识符。
- 你给出的代码是方法调用时传递新的参数，不涉及标识符的新增，因此它不算 "Adding an Identifier"。

# 没有hunk的修改文件, 文件状态`R100`，方法移动重构
`2535a4b531618dc2a5b43e1dc9390a002a4e9938`

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava b/src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava
rename to src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MetadataReader_getMetadataReader().mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MetadataReader_getMetadataReader().mjava b/src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MetadataReader_getMetadataReader().mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MetadataReader_getMetadataReader().mjava
rename to src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MetadataReader_getMetadataReader().mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#SubscriptionFactory_getSubscriptionFactory().mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#SubscriptionFactory_getSubscriptionFactory().mjava b/src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#SubscriptionFactory_getSubscriptionFactory().mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#SubscriptionFactory_getSubscriptionFactory().mjava
rename to src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#SubscriptionFactory_getSubscriptionFactory().mjava
```

# 发现了同一文件，一个hunk里删除一个hunk里增加相同内容，代码移动

`d72522598c61ca6d0d408ebceb14695311f26998`

```
====== DIFF: a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava ======
diff --git a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava b/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Set[Class]_getSuperclasses(Class).mjava
similarity index 96%
rename from src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava
rename to src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Set[Class]_getSuperclasses(Class).mjava
index 766fcb0..0bd1d4a 100644
--- a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava
+++ b/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Set[Class]_getSuperclasses(Class).mjava
@@ -1,6 +1,6 @@
 public	PUBLIC
 static	STATIC
-Collection	TYPENAME
+Set	TYPENAME
 <	LESS
 Class	TYPENAME
 >	GREAT
@@ -10,20 +10,27 @@ Class	TYPENAME
 from	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
-Collection	TYPENAME
+Set	TYPENAME
 <	LESS
 Class	TYPENAME
 >	GREAT
 superclasses	VARIABLENAME
 =	ASSIGN
 new	NEW
-LinkedList	TYPENAME
+HashSet	TYPENAME
 <	LESS
 Class	TYPENAME
 >	GREAT
 (	LEFTCLASSINSTANCECREATIONPAREN
 )	RIGHTCLASSINSTANCECREATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
+collectInterfaces	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+from	VARIABLENAME
+,	METHODINVOCATIONCOMMA
+superclasses	VARIABLENAME
+)	RIGHTMETHODINVOCATIONPAREN
+;	EXPRESSIONSTATEMENTSEMICOLON
 while	WHILE
 (	LEFTWHILEPAREN
 !	NOT
@@ -55,13 +62,6 @@ getSuperclass	INVOKEDMETHODNAME
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
-collectInterfaces	INVOKEDMETHODNAME
-(	LEFTMETHODINVOCATIONPAREN
-from	VARIABLENAME
-,	METHODINVOCATIONCOMMA
-superclasses	VARIABLENAME
-)	RIGHTMETHODINVOCATIONPAREN
-;	EXPRESSIONSTATEMENTSEMICOLON
 from	VARIABLENAME
 =	ASSIGN
 from	VARIABLENAME
```

`e55dcd1be5c6c59d597bd40c80bee03db1f36816`
```
====== DIFF: a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava ======
diff --git a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava b/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava
index eec52f9..766fcb0 100644
--- a/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava
+++ b/src/main/java/net/engio/mbassy/common/ReflectionUtils#public_Collection[Class]_getSuperclasses(Class).mjava
@@ -55,6 +55,13 @@ getSuperclass	INVOKEDMETHODNAME
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
+collectInterfaces	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+from	VARIABLENAME
+,	METHODINVOCATIONCOMMA
+superclasses	VARIABLENAME
+)	RIGHTMETHODINVOCATIONPAREN
+;	EXPRESSIONSTATEMENTSEMICOLON
 from	VARIABLENAME
 =	ASSIGN
 from	VARIABLENAME
@@ -64,13 +71,6 @@ getSuperclass	INVOKEDMETHODNAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 }	RIGHTWHILEBRACKET
-collectInterfaces	INVOKEDMETHODNAME
-(	LEFTMETHODINVOCATIONPAREN
-from	VARIABLENAME
-,	METHODINVOCATIONCOMMA
-superclasses	VARIABLENAME
-)	RIGHTMETHODINVOCATIONPAREN
-;	EXPRESSIONSTATEMENTSEMICOLON
 return	RETURN
 superclasses	VARIABLENAME
 ;	RETURNSTATEMENTSEMICOLON
```




# mjava的文件状态是Rxx,但hunk仅是replacing code，那就有可能是类名发生改变
`61d868dd4793f60c2cefbfe57a2edabd66231d6c`

```
====== DIFF: a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testStrongListenerSubscription().mjava ======
diff --git a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testStrongListenerSubscription().mjava b/src/test/java/net/engio/mbassy/SyncBusTest#public_void_testStrongListenerSubscription().mjava
similarity index 88%
rename from src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testStrongListenerSubscription().mjava
rename to src/test/java/net/engio/mbassy/SyncBusTest#public_void_testStrongListenerSubscription().mjava
index a363247..8ccfd6a 100644
--- a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testStrongListenerSubscription().mjava
+++ b/src/test/java/net/engio/mbassy/SyncBusTest#public_void_testStrongListenerSubscription().mjava
@@ -7,15 +7,11 @@ testStrongListenerSubscription	DECLAREDMETHODNAME
 throws	THROWS
 Exception	TYPENAME
 {	LEFTMETHODBRACKET
-MBassador	TYPENAME
+ISyncMessageBus	TYPENAME
 bus	VARIABLENAME
 =	ASSIGN
-getBus	INVOKEDMETHODNAME
+getSyncMessageBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-new	NEW
-BusConfiguration	TYPENAME
-(	LEFTCLASSINSTANCECREATIONPAREN
-)	RIGHTCLASSINSTANCECREATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 for	FOR
@@ -38,7 +34,7 @@ bus	VARIABLENAME
 subscribe	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 new	NEW
-EventingTestBean2	TYPENAME
+MessageListener2	TYPENAME
 (	LEFTCLASSINSTANCECREATIONPAREN
 )	RIGHTCLASSINSTANCECREATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
@@ -66,17 +62,25 @@ SubTestMessage	TYPENAME
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 bus	VARIABLENAME
 .	DOT
-publish	INVOKEDMETHODNAME
+post	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 message	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
+.	DOT
+now	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 bus	VARIABLENAME
 .	DOT
-publish	INVOKEDMETHODNAME
+post	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 subMessage	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
+.	DOT
+now	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 pause	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
```

```
====== DIFF: a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava ======
diff --git a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava b/src/test/java/net/engio/mbassy/SyncBusTest#public_void_testSynchronousMessagePublication().mjava
similarity index 89%
rename from src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava
rename to src/test/java/net/engio/mbassy/SyncBusTest#public_void_testSynchronousMessagePublication().mjava
index f6847b9..70b144a 100644
--- a/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava
+++ b/src/test/java/net/engio/mbassy/SyncBusTest#public_void_testSynchronousMessagePublication().mjava
@@ -7,15 +7,11 @@ testSynchronousMessagePublication	DECLAREDMETHODNAME
 throws	THROWS
 Exception	TYPENAME
 {	LEFTMETHODBRACKET
-MBassador	TYPENAME
+ISyncMessageBus	TYPENAME
 bus	VARIABLENAME
 =	ASSIGN
-getBus	INVOKEDMETHODNAME
+getSyncMessageBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-new	NEW
-BusConfiguration	TYPENAME
-(	LEFTCLASSINSTANCECREATIONPAREN
-)	RIGHTCLASSINSTANCECREATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 ListenerFactory	TYPENAME
@@ -30,7 +26,7 @@ create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
-EventingTestBean	TYPENAME
+MessageListener1	TYPENAME
 .	DOT
 class	CLASS
 )	RIGHTMETHODINVOCATIONPAREN
@@ -39,7 +35,7 @@ create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
-EventingTestBean2	TYPENAME
+MessageListener2	TYPENAME
 .	DOT
 class	CLASS
 )	RIGHTMETHODINVOCATIONPAREN
@@ -48,7 +44,7 @@ create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
-EventingTestBean3	TYPENAME
+MessageListener3	TYPENAME
 .	DOT
 class	CLASS
 )	RIGHTMETHODINVOCATIONPAREN
@@ -112,17 +108,25 @@ SubTestMessage	TYPENAME
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 bus	VARIABLENAME
 .	DOT
-publish	INVOKEDMETHODNAME
+post	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 message	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
+.	DOT
+now	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 bus	VARIABLENAME
 .	DOT
-publish	INVOKEDMETHODNAME
+post	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 subMessage	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
+.	DOT
+now	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 pause	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
```

# mjava文件名并不完整，比如
`4a3cb70ccbec732a7d823bd0d718aa3a16665cd1`

```
====== DIFF: a/src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],T,State).mjava ======
diff --git a/src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],T,State).mjava b/src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],Object,State).mjava
similarity index 97%
rename from src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],T,State).mjava
rename to src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],Object,State).mjava
index c30ddc0..ad3548a 100644
--- a/src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],T,State).mjava
+++ b/src/main/java/net/engio/mbassy/MessagePublication#private_MessagePublication(Collection[Subscription],Object,State).mjava
@@ -7,7 +7,7 @@ Subscription	TYPENAME
 >	GREAT
 subscriptions	VARIABLENAME
 ,	METHODDECLARAIONPARAMETERCOMMA
-T	TYPENAME
+Object	TYPENAME
 message	VARIABLENAME
 ,	METHODDECLARAIONPARAMETERCOMMA
 State	TYPENAME
```

# 有的hunk header相同，修改行数之类的一致，很可能是相同修改或者关联修改

```
bb390c67bdc2aab28af2e631432fea883473ee56

====== DIFF: a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_belongsTo(Class).mjava ======
diff --git a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_belongsTo(Class).mjava b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_belongsTo(Class).mjava
index c33b497..247246e 100644
--- a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_belongsTo(Class).mjava
+++ b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_belongsTo(Class).mjava
@@ -1,3 +1,8 @@
+/** 
+ * Check whether this subscription manages a message handler of the given message listener class
+ * @param listener
+ * @return
+ */	JAVADOCCOMMENT
 public	PUBLIC
 boolean	BOOLEAN
 belongsTo	DECLAREDMETHODNAME


====== DIFF: a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_contains(Object).mjava ======
diff --git a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_contains(Object).mjava b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_contains(Object).mjava
index caf79c8..2fce234 100644
--- a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_contains(Object).mjava
+++ b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_contains(Object).mjava
@@ -1,3 +1,8 @@
+/** 
+ * Check whether this subscriptions manages the given listener instance
+ * @param listener
+ * @return
+ */	JAVADOCCOMMENT
 public	PUBLIC
 boolean	BOOLEAN
 contains	DECLAREDMETHODNAME

====== DIFF: a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_handlesMessageType(Class[#]).mjava ======
diff --git a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_handlesMessageType(Class[#]).mjava b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_handlesMessageType(Class[#]).mjava
index 98c14af..8886941 100644
--- a/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_handlesMessageType(Class[#]).mjava
+++ b/src/main/java/net/engio/mbassy/subscription/Subscription#public_boolean_handlesMessageType(Class[#]).mjava
@@ -1,3 +1,8 @@
+/** 
+ * Check whether this subscription manages a message handler
+ * @param messageType
+ * @return
+ */	JAVADOCCOMMENT
 public	PUBLIC
 boolean	BOOLEAN
 handlesMessageType	DECLAREDMETHODNAME

```

# 同一个文件修改记录，一个修改了方法签名里的参数类型和参数名，另一个相应修改了使用时的参数名

```
bb390c67bdc2aab28af2e631432fea883473ee56

====== DIFF: a/src/main/java/net/engio/mbassy/listener/MessageListenerMetadata#public_boolean_addHandler(MessageHandlerMetadata).mjava ======
diff --git a/src/main/java/net/engio/mbassy/listener/MessageListenerMetadata#public_boolean_addHandler(MessageHandlerMetadata).mjava b/src/main/java/net/engio/mbassy/listener/MessageListener#public_boolean_addHandler(MessageHandler).mjava
similarity index 73%
rename from src/main/java/net/engio/mbassy/listener/MessageListenerMetadata#public_boolean_addHandler(MessageHandlerMetadata).mjava
rename to src/main/java/net/engio/mbassy/listener/MessageListener#public_boolean_addHandler(MessageHandler).mjava
index f982acf..0f1de07 100644
--- a/src/main/java/net/engio/mbassy/listener/MessageListenerMetadata#public_boolean_addHandler(MessageHandlerMetadata).mjava
+++ b/src/main/java/net/engio/mbassy/listener/MessageListener#public_boolean_addHandler(MessageHandler).mjava
@@ -2,8 +2,8 @@ public	PUBLIC
 boolean	BOOLEAN
 addHandler	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
-MessageHandlerMetadata	TYPENAME
-messageHandlerMetadata	VARIABLENAME
+MessageHandler	TYPENAME
+messageHandler	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
 return	RETURN
@@ -11,7 +11,7 @@ handlers	VARIABLENAME
 .	DOT
 add	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-messageHandlerMetadata	VARIABLENAME
+messageHandler	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	RETURNSTATEMENTSEMICOLON
 }	RIGHTMETHODBRACKET
```

# 同一个文件，一个hunk修改了方法名，另一个用方法名做类型的变量类型修改了

```

bb390c67bdc2aab28af2e631432fea883473ee56
====== DIFF: a/src/main/java/net/engio/mbassy/listener/MessageHandlerMetadata#public_MessageHandlerMetadata(Method,IMessageFilter[],Handler,MessageListenerMetadata).mjava ======
diff --git a/src/main/java/net/engio/mbassy/listener/MessageHandlerMetadata#public_MessageHandlerMetadata(Method,IMessageFilter[],Handler,MessageListenerMetadata).mjava b/src/main/java/net/engio/mbassy/listener/MessageHandler#public_MessageHandler(Method,IMessageFilter[],Handler,MessageListener).mjava
similarity index 97%
rename from src/main/java/net/engio/mbassy/listener/MessageHandlerMetadata#public_MessageHandlerMetadata(Method,IMessageFilter[],Handler,MessageListenerMetadata).mjava
rename to src/main/java/net/engio/mbassy/listener/MessageHandler#public_MessageHandler(Method,IMessageFilter[],Handler,MessageListener).mjava
index 3291daa..300e93c 100644
--- a/src/main/java/net/engio/mbassy/listener/MessageHandlerMetadata#public_MessageHandlerMetadata(Method,IMessageFilter[],Handler,MessageListenerMetadata).mjava
+++ b/src/main/java/net/engio/mbassy/listener/MessageHandler#public_MessageHandler(Method,IMessageFilter[],Handler,MessageListener).mjava
@@ -1,5 +1,5 @@
 public	PUBLIC
-MessageHandlerMetadata	DECLAREDMETHODNAME
+MessageHandler	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 Method	TYPENAME
 handler	VARIABLENAME
@@ -12,7 +12,7 @@ filter	VARIABLENAME
 Handler	TYPENAME
 handlerConfig	VARIABLENAME
 ,	METHODDECLARAIONPARAMETERCOMMA
-MessageListenerMetadata	TYPENAME
+MessageListener	TYPENAME
 listenerConfig	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
```

# 类名变化，文件名没变化，文件修改和类名无关，单纯移动方法和其他文件名无关修改
`f78be61bb2698c70f33ad58fbebb625e2987b172`
```
====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
similarity index 94%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
index a80ec63..de1ae40 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testSimpleStringCondition	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
```

```
ce80e8b4e2a2affc4965fc96824d3dfd00dd13a3

====== DIFF: a/src/test/java/org/mbassy/MBassadorTest#public_void_testConcurrentMixedMessagePublication().mjava ======
diff --git a/src/test/java/org/mbassy/MBassadorTest#public_void_testConcurrentMixedMessagePublication().mjava b/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testConcurrentMixedMessagePublication().mjava
similarity index 96%
rename from src/test/java/org/mbassy/MBassadorTest#public_void_testConcurrentMixedMessagePublication().mjava
rename to src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testConcurrentMixedMessagePublication().mjava
index 84547e5..629bada 100644
--- a/src/test/java/org/mbassy/MBassadorTest#public_void_testConcurrentMixedMessagePublication().mjava
+++ b/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testConcurrentMixedMessagePublication().mjava
@@ -66,7 +66,7 @@ ListenerFactory	TYPENAME
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean	TYPENAME
 .	DOT
@@ -75,7 +75,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean2	TYPENAME
 .	DOT
@@ -84,7 +84,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean3	TYPENAME
 .	DOT
@@ -93,7 +93,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 Object	TYPENAME
 .	DOT
@@ -102,7 +102,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 NonListeningBean	TYPENAME
 .	DOT
@@ -216,7 +216,7 @@ subEvent	VARIABLENAME
 ;	EXPRESSIONSTATEMENTSEMICOLON
 pause	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-3000	NUMBERLITERAL
+processingTimeInMS	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 for	FOR
@@ -229,7 +229,7 @@ testEvents	VARIABLENAME
 {	LEFTENHANCEDFORBRACKET
 assertEquals	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-300	NUMBERLITERAL
+30000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 event	VARIABLENAME
 .	DOT
@@ -251,7 +251,7 @@ subtestEvents	VARIABLENAME
 {	LEFTENHANCEDFORBRACKET
 assertEquals	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-700	NUMBERLITERAL
+70000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 event	VARIABLENAME
 .	DOT

====== DIFF: a/src/test/java/org/mbassy/MBassadorTest#public_void_testSynchronousMessagePublication().mjava ======
diff --git a/src/test/java/org/mbassy/MBassadorTest#public_void_testSynchronousMessagePublication().mjava b/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava
similarity index 95%
rename from src/test/java/org/mbassy/MBassadorTest#public_void_testSynchronousMessagePublication().mjava
rename to src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava
index 48cf12f..d765c55 100644
--- a/src/test/java/org/mbassy/MBassadorTest#public_void_testSynchronousMessagePublication().mjava
+++ b/src/test/java/net/engio/mbassy/MessagePublicationTest#public_void_testSynchronousMessagePublication().mjava
@@ -29,7 +29,7 @@ ListenerFactory	TYPENAME
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean	TYPENAME
 .	DOT
@@ -38,7 +38,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean2	TYPENAME
 .	DOT
@@ -47,7 +47,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 EventingTestBean3	TYPENAME
 .	DOT
@@ -56,7 +56,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 Object	TYPENAME
 .	DOT
@@ -65,7 +65,7 @@ class	CLASS
 .	DOT
 create	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-100	NUMBERLITERAL
+10000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 NonListeningBean	TYPENAME
 .	DOT
@@ -127,12 +127,12 @@ subEvent	VARIABLENAME
 ;	EXPRESSIONSTATEMENTSEMICOLON
 pause	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-2000	NUMBERLITERAL
+processingTimeInMS	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 assertEquals	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-300	NUMBERLITERAL
+30000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 event	VARIABLENAME
 .	DOT
@@ -145,7 +145,7 @@ get	INVOKEDMETHODNAME
 ;	EXPRESSIONSTATEMENTSEMICOLON
 assertEquals	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-700	NUMBERLITERAL
+70000	NUMBERLITERAL
 ,	METHODINVOCATIONCOMMA
 subEvent	VARIABLENAME
 .	DOT
```




# 不同文件，相同hunk修改
`f78be61bb2698c70f33ad58fbebb625e2987b172`
```
====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleCombinedEL().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleCombinedEL().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleCombinedEL().mjava
similarity index 94%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleCombinedEL().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleCombinedEL().mjava
index 9ce666c..532def1 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleCombinedEL().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleCombinedEL().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testHandleCombinedEL	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON

====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleMethodAccessEL().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleMethodAccessEL().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleMethodAccessEL().mjava
similarity index 94%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleMethodAccessEL().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleMethodAccessEL().mjava
index cf95cd1..d74bba0 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testHandleMethodAccessEL().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testHandleMethodAccessEL().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testHandleMethodAccessEL	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON

====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testNotMatchingAnyCondition().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testNotMatchingAnyCondition().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testNotMatchingAnyCondition().mjava
similarity index 93%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testNotMatchingAnyCondition().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testNotMatchingAnyCondition().mjava
index 6c0b229..3e9947e 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testNotMatchingAnyCondition().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testNotMatchingAnyCondition().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testNotMatchingAnyCondition	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON

====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleNumberCondition().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleNumberCondition().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleNumberCondition().mjava
similarity index 94%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleNumberCondition().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleNumberCondition().mjava
index 1e9afff..2d17c11 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleNumberCondition().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleNumberCondition().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testSimpleNumberCondition	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON

====== DIFF: a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava ======
diff --git a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
similarity index 94%
rename from src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava
rename to src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
index a80ec63..de1ae40 100644
--- a/src/test/java/net/engio/mbassy/ConditionalHandlers#public_void_testSimpleStringCondition().mjava
+++ b/src/test/java/net/engio/mbassy/ConditionalHandlerTest#public_void_testSimpleStringCondition().mjava
@@ -1,14 +1,9 @@
-/** 
- * @throws Exception
- */	JAVADOCCOMMENT
 @Test	ANNOTATION
 public	PUBLIC
 void	VOID
 testSimpleStringCondition	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 )	RIGHTMETHODPAREN
-throws	THROWS
-Exception	TYPENAME
 {	LEFTMETHODBRACKET
 MBassador	TYPENAME
 bus	VARIABLENAME
@@ -17,7 +12,6 @@ createBus	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 SyncAsync	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-false	FALSE
 )	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON


```
# 这种代码我之前标注的的是``replacing code`,但现在我标注的是`changing identifer type`

```
====== DIFF: a/src/test/java/net/engio/mbassy/common/MessageBusTest#public_void_setUp().mjava ======
diff --git a/src/test/java/net/engio/mbassy/common/MessageBusTest#public_void_setUp().mjava b/src/test/java/net/engio/mbassy/common/MessageBusTest#public_void_setUp().mjava
index da8e248..25fa9a4 100644
--- a/src/test/java/net/engio/mbassy/common/MessageBusTest#public_void_setUp().mjava
+++ b/src/test/java/net/engio/mbassy/common/MessageBusTest#public_void_setUp().mjava
@@ -10,7 +10,7 @@ issuedPublications	VARIABLENAME
 new	NEW
 StrongConcurrentSet	TYPENAME
 <	LESS
-MessagePublication	TYPENAME
+IMessagePublication	TYPENAME
 >	GREAT
 (	LEFTCLASSINSTANCECREATIONPAREN
 )	RIGHTCLASSINSTANCECREATIONPAREN
```
