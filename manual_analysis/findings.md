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

# Different path, different files, similar modifications.
```
cc6cc217cc14dedd2767c686bb91b064213f2f75
636ca09e9ed091efabc7784661e8f0994175c73d
636ca09e9ed091efabc7784661e8f0994175c73d
```




# Files without hunk modifications, file status `R100`, method move refactoring.
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

# Found in the same file: one hunk deletes and another hunk adds the same content, indicating code movement.

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




# If the `.mjava` file status is `Rxx`, but the hunk only involves replacing code, it is likely that the class name or file path has changed. In any case, the modification is unrelated to file renaming.
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

# The `.mjava` filenames are not complete, for example:
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

# Some hunk headers are identical, with the same number of modified lines, which likely indicates the same modification or related modifications.

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

# In the same file's modification record, one change updates the parameter type and name in the method signature, while another correspondingly updates the parameter name in its usage.

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

# In the same file, one hunk renames a method, while another modifies a related parameter type, suggesting a consistent naming refactor.

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

# Class name changed, but the file name remained unchanged. The file modification is unrelated to the class name. Methods were simply moved, and the modifications are unrelated to other file names.
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




# Different files, same hunk modifications.
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





# FINDINGS & Problems
```
1. Move Method Refactoring
Analyze the file modification records processed by FinerGit. If the file status is "R100" and contains no hunks, it can be inferred that there is a "Move Method" refactoring.
For example: commit_id:2535a4b531618dc2a5b43e1dc9390a002a4e9938
====== DIFF======
diff --git a/src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava b/src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/config/IBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava
rename to src/main/java/net/engio/mbassy/bus/config/ISyncBusConfiguration#MessagePublication.Factory_getMessagePublicationFactory().mjava
====== DIFF======

====== ORIGINAL======
The corresponding modification records for the original file are as follows:
commit_id, file_status, old_filename, new_filename
52f52864de3a0b9fc9b6a0459370f63a18510834, M, src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus.java, NULL
====== ORIGINAL======

2. Analyze the file modification records processed by FinerGit. If the file status is "Rxx" and contains hunks with minor changes, marked as part of the "Changing Identifiers" series, "Changing Return Type," or "Changing Access Modifier," it can be inferred that there is a "Changing Parameter," "Changing Return Type," or "Changing Access Modifier" refactoring. All of these changes modify the method signature.

3. Analyze the file modification records processed by FinerGit. If the file status is M and contains hunks, but the hunks are marked as part of the "Changing Method Modifier" series, during manual analysis, I found that the "mjava" filenames processed by FinerGit do not include the Method Modifier. Therefore, even though the file status is M, the method signature has actually been changed. It can be inferred that there is a "Changing Method Modifier" series refactoring.

4. Analyze the file modification records processed by FinerGit. If the file status is M and contains hunks and the hunks are marked as part of the "Changing Annotation" series, it can be inferred that there is a "Changing Annotation" series refactoring.

5. Two hunks added and removed the same code in the diff of the same file modification, but it doesn't seem closely related to code cloning or refactoring.

6. I haven't performed a content comparison or manually checked the contents of the "file created" and "file removed" hunks for now. As for the hunks marked as "Removing Code" and "Adding Code," I have only found one set of similar codes being added, removed, or moved (Project 5). In the future, using the `diff_lines` data table for content comparison might reveal more meaningful code behavior.
The hunks information I currently output includes the corresponding diff information for the mjava files processed by FinerGit. I initially intended also to output the diff information for the original files, but due to the difficulty in matching Java file paths with mjava file paths, I haven't achieved this goal yet. For now, I can only manually retrieve the diff information for the original files.

7. If the file status is “M” but the hunks are “changing identifiers”, I think it can be inferred that they are “change
variable” refactoring. I will continue to organize my findings later.

```
