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
## tokenized log
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

## original log

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

---
| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | 294461c | 55 | Rename Method | 'protected_MessagePublication_addAsynchronousDeliveryRequest' to 'protected_MessagePublication_addAsynchronousPublication' at 'src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus' | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication).mjava | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication).mjava |
| mbassador | 294461c | 60 | Rename Method | 'protected_MessagePublication_addAsynchronousDeliveryRequest' to 'protected_MessagePublication_addAsynchronousPublication' at 'src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus' | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousDeliveryRequest(MessagePublication,long,TimeUnit).mjava | src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus#protected_MessagePublication_addAsynchronousPublication(MessagePublication,long,TimeUnit).mjava |

# Rename Method
- same path, same class name, different method name

## tokenized log
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
## original log

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus.java ======
diff --git a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus.java b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus.java
index d4187d1..d6b7e27 100644
--- a/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus.java
+++ b/src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageBus.java
@@ -17,7 +17,8 @@ import java.util.concurrent.TimeUnit;
  * @param <T>
  * @param <P>
  */
-public abstract class AbstractSyncAsyncMessageBus<T, P extends ISyncAsyncPublicationCommand> extends AbstractSyncMessageBus<T, P> implements IMessageBus<T, P> {
+public abstract class AbstractSyncAsyncMessageBus<T, P extends ISyncAsyncPublicationCommand>
+        extends AbstractPubSubSupport<T> implements IMessageBus<T, P> {
 
     // executor for asynchronous message handlers
     private final ExecutorService executor;
@@ -47,13 +48,15 @@ public abstract class AbstractSyncAsyncMessageBus<T, P extends ISyncAsyncPublica
             Thread dispatcher = configuration.getThreadFactoryForAsynchronousMessageDispatch().newThread(new Runnable() {
                 public void run() {
                     while (true) {
+                        MessagePublication publication = null;
                         try {
-                            pendingMessages.take().execute();
+                            publication = pendingMessages.take();
+                            publication.execute();
                         } catch (InterruptedException e) {
                             Thread.currentThread().interrupt();
                             return;
                         } catch(Throwable t){
-                            handlePublicationError(new PublicationError(t, "Error in asynchronous dispatch", null, null, null));
+                            handlePublicationError(new PublicationError(t, "Error in asynchronous dispatch",publication));
                         }
                     }
                 }
@@ -64,26 +67,26 @@ public abstract class AbstractSyncAsyncMessageBus<T, P extends ISyncAsyncPublica
     }
 
 
-    // this method enqueues a message delivery request
-    protected MessagePublication addAsynchronousDeliveryRequest(MessagePublication request) {
+    // this method queues a message delivery request
+    protected MessagePublication addAsynchronousPublication(MessagePublication publication) {
         try {
-            pendingMessages.put(request);
-            return request.markScheduled();
+            pendingMessages.put(publication);
+            return publication.markScheduled();
         } catch (InterruptedException e) {
-            // TODO: publication error
-            return request;
+            handlePublicationError(new PublicationError(e, "Error while adding an asynchronous message publication", publication));
+            return publication;
         }
     }
 
     // this method queues a message delivery request
-    protected MessagePublication addAsynchronousDeliveryRequest(MessagePublication request, long timeout, TimeUnit unit) {
+    protected MessagePublication addAsynchronousPublication(MessagePublication publication, long timeout, TimeUnit unit) {
         try {
-            return pendingMessages.offer(request, timeout, unit)
-                    ? request.markScheduled()
-                    : request;
+            return pendingMessages.offer(publication, timeout, unit)
+                    ? publication.markScheduled()
+                    : publication;
         } catch (InterruptedException e) {
-            // TODO: publication error
-            return request;
+            handlePublicationError(new PublicationError(e, "Error while adding an asynchronous message publication", publication));
+            return publication;
         }
     }
```

- Associated Modifications

**tokenized log**

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T,long,TimeUnit).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T,long,TimeUnit).mjava b/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T,long,TimeUnit).mjava
index 2e0bd9f..919006f 100644
--- a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T,long,TimeUnit).mjava
+++ b/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T,long,TimeUnit).mjava
@@ -14,7 +14,7 @@ unit	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
 return	RETURN
-addAsynchronousDeliveryRequest	INVOKEDMETHODNAME
+addAsynchronousPublication	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 createMessagePublication	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
```

```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T).mjava ======
diff --git a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T).mjava b/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T).mjava
index cb66d7a..dd2777f 100644
--- a/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T).mjava
+++ b/src/main/java/net/engio/mbassy/bus/MBassador#public_MessagePublication_publishAsync(T).mjava
@@ -8,7 +8,7 @@ message	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
 return	RETURN
-addAsynchronousDeliveryRequest	INVOKEDMETHODNAME
+addAsynchronousPublication	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 createMessagePublication	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
```


**original log**
```
====== DIFF: a/src/main/java/net/engio/mbassy/bus/MBassador.java ======
diff --git a/src/main/java/net/engio/mbassy/bus/MBassador.java b/src/main/java/net/engio/mbassy/bus/MBassador.java
index e99f937..ee4206f 100644
--- a/src/main/java/net/engio/mbassy/bus/MBassador.java
+++ b/src/main/java/net/engio/mbassy/bus/MBassador.java
@@ -16,12 +16,12 @@ public class MBassador<T> extends AbstractSyncAsyncMessageBus<T, SyncAsyncPostCo
 
     @Override
     public MessagePublication publishAsync(T message) {
-        return addAsynchronousDeliveryRequest(createMessagePublication(message));
+        return addAsynchronousPublication(createMessagePublication(message));
     }
 
     @Override
     public MessagePublication publishAsync(T message, long timeout, TimeUnit unit) {
-        return addAsynchronousDeliveryRequest(createMessagePublication(message), timeout, unit);
+        return addAsynchronousPublication(createMessagePublication(message), timeout, unit);
     }
```

---
| **Refactoring Type**         | **Detailed Changes** |
|-----------------------------|------------------------------------------------------------|
| **Move Method**              |  |
| **Rename Method** |  |

</details>
