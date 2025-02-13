<details>
<summary>294461c978700aae933fe9975f1ea3ceda147e0a</summary>

| **hayashi Type**         | **Count** |
|-----------------------------|----------|
| **Move Method**             | 6        |
| **Rename Method**           | 2        |
| **Move and Rename Method**  | 1        |  

| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | 294461c | 100 | Move Method | 'protected_Collection[Subscription]_getSubscriptionsByMessageType' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava |
| mbassador | 294461c | 100 | Move Method | 'protected_MessagePublication_createMessagePublication' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_MessagePublication_createMessagePublication(T).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_MessagePublication_createMessagePublication(T).mjava |
| mbassador | 294461c | 100 | Move Method | 'public_boolean_unsubscribe' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_boolean_unsubscribe(Object).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_boolean_unsubscribe(Object).mjava |
| mbassador | 294461c | 100 | Move Method | 'public_void_addErrorHandler' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_addErrorHandler(IPublicationErrorHandler).mjava |
| mbassador | 294461c | 100 | Move Method | 'public_void_handlePublicationError' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_handlePublicationError(PublicationError).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_handlePublicationError(PublicationError).mjava |
| mbassador | 294461c | 100 | Move Method | 'public_void_subscribe' from 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_subscribe(Object).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_subscribe(Object).mjava |
| mbassador | 294461c | 97 | Move and Rename Method | 'public_AbstractSyncMessageBus' at 'src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus' to 'public_AbstractPubSubSupport' at 'src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport' | src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_AbstractSyncMessageBus(ISyncBusConfiguration).mjava | src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_AbstractPubSubSupport(ISyncBusConfiguration).mjava |


# Move Method

- same path, different class name

## tokenized log
```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_MessagePublication_createMessagePublication(T).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_MessagePublication_createMessagePublication(T).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_MessagePublication_createMessagePublication(T).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#protected_MessagePublication_createMessagePublication(T).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#protected_MessagePublication_createMessagePublication(T).mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_boolean_unsubscribe(Object).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_boolean_unsubscribe(Object).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_boolean_unsubscribe(Object).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_boolean_unsubscribe(Object).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_boolean_unsubscribe(Object).mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_addErrorHandler(IPublicationErrorHandler).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_addErrorHandler(IPublicationErrorHandler).mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_handlePublicationError(PublicationError).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_handlePublicationError(PublicationError).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_handlePublicationError(PublicationError).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_handlePublicationError(PublicationError).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_handlePublicationError(PublicationError).mjava

====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_subscribe(Object).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_subscribe(Object).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_subscribe(Object).mjava
similarity index 100%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_void_subscribe(Object).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_void_subscribe(Object).mjava
```
# Move and Rename Method

- same path, different class name, different method name

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_AbstractSyncMessageBus(ISyncBusConfiguration).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_AbstractSyncMessageBus(ISyncBusConfiguration).mjava b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_AbstractPubSubSupport(ISyncBusConfiguration).mjava
similarity index 97%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_AbstractSyncMessageBus(ISyncBusConfiguration).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_AbstractPubSubSupport(ISyncBusConfiguration).mjava
index 6ab376d..ec96777 100644
--- a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus#public_AbstractSyncMessageBus(ISyncBusConfiguration).mjava
+++ b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#public_AbstractPubSubSupport(ISyncBusConfiguration).mjava
@@ -1,5 +1,5 @@
 public	PUBLIC
-AbstractSyncMessageBus	DECLAREDMETHODNAME
+AbstractPubSubSupport	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 ISyncBusConfiguration	TYPENAME
 configuration	VARIABLENAME
```

# original log

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus.java ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus.java b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport.java
similarity index 91%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus.java
rename to src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport.java
index 164affc..e74be6f 100644
--- a/src/main/java/net/engio/mbassy/bus/AbstractSyncMessageBus.java
+++ b/src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport.java
@@ -3,7 +3,6 @@ package net.engio.mbassy.bus;
 import net.engio.mbassy.IPublicationErrorHandler;
 import net.engio.mbassy.PublicationError;
 import net.engio.mbassy.bus.config.ISyncBusConfiguration;
-import net.engio.mbassy.bus.publication.IPublicationCommand;
 import net.engio.mbassy.common.DeadMessage;
 import net.engio.mbassy.subscription.Subscription;
 import net.engio.mbassy.subscription.SubscriptionManager;
@@ -17,9 +16,8 @@ import java.util.List;
  * The base class for all message bus implementations.
  *
  * @param <T>
- * @param <P>
  */
-public abstract class AbstractSyncMessageBus<T, P extends IPublicationCommand> implements ISyncMessageBus<T, P>{
+public abstract class AbstractPubSubSupport<T> implements PubSubSupport<T>{
 
 
     // this handler will receive all errors that occur during message dispatch or message handling
@@ -32,7 +30,7 @@ public abstract class AbstractSyncMessageBus<T, P extends IPublicationCommand> i
     private final BusRuntime runtime;
 
 
-    public AbstractSyncMessageBus(ISyncBusConfiguration configuration) {
+    public AbstractPubSubSupport(ISyncBusConfiguration configuration) {
         this.runtime = new BusRuntime(this);
         this.runtime.add("error.handlers", getRegisteredErrorHandlers());
         this.subscriptionManager = configuration.getSubscriptionManagerProvider()
@@ -45,7 +43,7 @@ public abstract class AbstractSyncMessageBus<T, P extends IPublicationCommand> i
         return publicationFactory;
     }
 
-    @Override
+
     public Collection<IPublicationErrorHandler> getRegisteredErrorHandlers() {
         return Collections.unmodifiableCollection(errorHandlers);
     }
```

- Associated Modifications


```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/SyncMessageBus.java ======
diff --git a/src/main/java/net/engio/mbassy/bus/SyncMessageBus.java b/src/main/java/net/engio/mbassy/bus/SyncMessageBus.java
index 72c45f4..9dfb911 100644
--- a/src/main/java/net/engio/mbassy/bus/SyncMessageBus.java
+++ b/src/main/java/net/engio/mbassy/bus/SyncMessageBus.java
@@ -5,25 +5,18 @@ import net.engio.mbassy.bus.config.ISyncBusConfiguration;
 import net.engio.mbassy.bus.publication.IPublicationCommand;
 
 /**
- * Created with IntelliJ IDEA.
- * User: benjamin
- * Date: 4/3/13
- * Time: 9:02 AM
- * To change this template use File | Settings | File Templates.
+ * A message bus implementation that offers only synchronous message publication. Using this bus
+ * will not create any new threads.
+ *
  */
-public class SyncMessageBus<T> extends AbstractSyncMessageBus<T, SyncMessageBus.SyncPostCommand>{
+public class SyncMessageBus<T> extends AbstractPubSubSupport<T> implements ISyncMessageBus<T, SyncMessageBus.SyncPostCommand>{
 
 
     public SyncMessageBus(ISyncBusConfiguration configuration) {
         super(configuration);
     }
 
-    /**
-     * Synchronously publish a message to all registered listeners (this includes listeners defined for super types)
-     * The call blocks until every messageHandler has processed the message.
-     *
-     * @param message
-     */
+    @Override
     public void publish(T message) {
         try {
             MessagePublication publication = createMessagePublication(message);
@@ -34,7 +27,6 @@ public class SyncMessageBus<T> extends AbstractSyncMessageBus<T, SyncMessageBus.
                     .setCause(e)
                     .setPublishedObject(message));
         }
-
     }
 
     @Override
@@ -44,7 +36,6 @@ public class SyncMessageBus<T> extends AbstractSyncMessageBus<T, SyncMessageBus.
 
     public class SyncPostCommand implements IPublicationCommand {
 
-
         private T message;
 
         public SyncPostCommand(T message) {
```


| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | 294461c | 55 | Rename Method | 'protected_MessagePublication_addAsynchronousDeliveryRequest' to 'protected_MessagePublication_addAsynchronousPublication' at 'src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus' | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication).mjava |
| mbassador | 294461c | 60 | Rename Method | 'protected_MessagePublication_addAsynchronousDeliveryRequest' to 'protected_MessagePublication_addAsynchronousPublication' at 'src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus' | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication,long,TimeUnit).mjava |

# Rename Method
- same path, same class name, different method name

# tokenized log
- R55

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication).mjava
similarity index 55%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication).mjava
index a989e7a..7202100 100644
--- a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava
+++ b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication).mjava
@@ -1,9 +1,9 @@
 protected	PROTECTED
 MessagePublication	TYPENAME
-addAsynchronousDeliveryRequest	DECLAREDMETHODNAME
+addAsynchronousPublication	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 MessagePublication	TYPENAME
-request	VARIABLENAME
+publication	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
 try	TRY
@@ -12,11 +12,11 @@ pendingMessages	VARIABLENAME
 .	DOT
 put	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-request	VARIABLENAME
+publication	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 return	RETURN
-request	VARIABLENAME
+publication	VARIABLENAME
 .	DOT
 markScheduled	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
@@ -29,8 +29,21 @@ InterruptedException	TYPENAME
 e	VARIABLENAME
 )	RIGHTCATCHCLAUSEPAREN
 {	LEFTCATCHCLAUSEBRACKET
+handlePublicationError	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+new	NEW
+PublicationError	TYPENAME
+(	LEFTCLASSINSTANCECREATIONPAREN
+e	VARIABLENAME
+,	CLASSINSTANCECREATIONCOMMA
+"Error while adding an asynchronous message publication"	STRINGLITERAL
+,	CLASSINSTANCECREATIONCOMMA
+publication	VARIABLENAME
+)	RIGHTCLASSINSTANCECREATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
+;	EXPRESSIONSTATEMENTSEMICOLON
 return	RETURN
-request	VARIABLENAME
+publication	VARIABLENAME
 ;	RETURNSTATEMENTSEMICOLON
 }	RIGHTCATCHCLAUSEBRACKET
 }	RIGHTMETHODBRACKET
```

- R60

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication,long,TimeUnit).mjava
similarity index 60%
rename from src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava
rename to src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication,long,TimeUnit).mjava
index 8fa9250..57ad85f 100644
--- a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava
+++ b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication,long,TimeUnit).mjava
@@ -1,9 +1,9 @@
 protected	PROTECTED
 MessagePublication	TYPENAME
-addAsynchronousDeliveryRequest	DECLAREDMETHODNAME
+addAsynchronousPublication	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 MessagePublication	TYPENAME
-request	VARIABLENAME
+publication	VARIABLENAME
 ,	METHODDECLARAIONPARAMETERCOMMA
 long	LONG
 timeout	VARIABLENAME
@@ -19,20 +19,20 @@ pendingMessages	VARIABLENAME
 .	DOT
 offer	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
-request	VARIABLENAME
+publication	VARIABLENAME
 ,	METHODINVOCATIONCOMMA
 timeout	VARIABLENAME
 ,	METHODINVOCATIONCOMMA
 unit	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ?	QUESTION
-request	VARIABLENAME
+publication	VARIABLENAME
 .	DOT
 markScheduled	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 :	COLON
-request	VARIABLENAME
+publication	VARIABLENAME
 ;	RETURNSTATEMENTSEMICOLON
 }	RIGHTTRYBRACKET
 catch	CATCH
@@ -41,8 +41,21 @@ InterruptedException	TYPENAME
 e	VARIABLENAME
 )	RIGHTCATCHCLAUSEPAREN
 {	LEFTCATCHCLAUSEBRACKET
+handlePublicationError	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
+new	NEW
+PublicationError	TYPENAME
+(	LEFTCLASSINSTANCECREATIONPAREN
+e	VARIABLENAME
+,	CLASSINSTANCECREATIONCOMMA
+"Error while adding an asynchronous message publication"	STRINGLITERAL
+,	CLASSINSTANCECREATIONCOMMA
+publication	VARIABLENAME
+)	RIGHTCLASSINSTANCECREATIONPAREN
+)	RIGHTMETHODINVOCATIONPAREN
+;	EXPRESSIONSTATEMENTSEMICOLON
 return	RETURN
-request	VARIABLENAME
+publication	VARIABLENAME
 ;	RETURNSTATEMENTSEMICOLON
 }	RIGHTCATCHCLAUSEBRACKET
 }	RIGHTMETHODBRACKET
```

