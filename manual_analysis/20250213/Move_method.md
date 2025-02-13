<details>
<summary>ce80e8b4e2a2affc4965fc96824d3dfd00dd13a3</summary>

### Three types 
| Path Change | Class Name Change | Count |
|----------------------------|----------------------------|-------|
| Different paths | Same class name | 109 |
| Different paths | Different class names | 1 |
| Same path | Different class name | 0 |

### Different paths, same class name


| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | ce80e8b | 100 | Move Method | 'private_void_addMessageTypeSubscription' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'private_void_initDispatcherThreads' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'protected_Collection[Subscription]_getSubscriptionsByMessageType' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'protected_MessagePublication[T]_addAsynchronousDeliveryRequest' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'protected_MessagePublication[T]_addAsynchronousDeliveryRequest' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'public_AbstractMessageBus' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'public_boolean_unsubscribe' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'public_void_addErrorHandler' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'public_void_handlePublicationError' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava |
| mbassador | ce80e8b | 100 | Move Method | 'public_void_subscribe' from 'src/main/java/org/mbassy/AbstractMessageBus' to 'src/main/java/net/engio/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava | src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava |

#### tokenized log

```
====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#private_void_shutdown().mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#private_void_shutdown().mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_shutdown().mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#private_void_shutdown().mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#private_void_shutdown().mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T]).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#protected_MessagePublication[T]_addAsynchronousDeliveryRequest(MessagePublication[T],long,TimeUnit).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#protected_void_finalize().mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#protected_void_finalize().mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#protected_void_finalize().mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#protected_void_finalize().mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#protected_void_finalize().mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_AbstractMessageBus(BusConfiguration).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_Collection[IPublicationErrorHandler]_getRegisteredErrorHandlers().mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_Collection[IPublicationErrorHandler]_getRegisteredErrorHandlers().mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_Collection[IPublicationErrorHandler]_getRegisteredErrorHandlers().mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_Collection[IPublicationErrorHandler]_getRegisteredErrorHandlers().mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_Collection[IPublicationErrorHandler]_getRegisteredErrorHandlers().mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_Executor_getExecutor().mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_Executor_getExecutor().mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_Executor_getExecutor().mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_Executor_getExecutor().mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_Executor_getExecutor().mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_boolean_hasPendingMessages().mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_boolean_hasPendingMessages().mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_boolean_hasPendingMessages().mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_boolean_hasPendingMessages().mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_boolean_hasPendingMessages().mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_boolean_unsubscribe(Object).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava

====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava b/src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava
similarity index 100%
rename from src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava
rename to src/main/java/net/engio/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava

```

#### original log

```
====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus.java ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus.java b/src/main/java/net/engio/mbassy/AbstractMessageBus.java
similarity index 96%
rename from src/main/java/org/mbassy/AbstractMessageBus.java
rename to src/main/java/net/engio/mbassy/AbstractMessageBus.java
index e9c72c6..e8d9897 100644
--- a/src/main/java/org/mbassy/AbstractMessageBus.java
+++ b/src/main/java/net/engio/mbassy/AbstractMessageBus.java
@@ -1,15 +1,14 @@
-package org.mbassy;
+package net.engio.mbassy;
 
-import org.mbassy.common.ReflectionUtils;
-import org.mbassy.dispatch.MessagingContext;
-import org.mbassy.listener.MessageHandlerMetadata;
-import org.mbassy.listener.MetadataReader;
-import org.mbassy.subscription.Subscription;
-import org.mbassy.subscription.SubscriptionFactory;
+import net.engio.mbassy.common.ReflectionUtils;
+import net.engio.mbassy.dispatch.MessagingContext;
+import net.engio.mbassy.listener.MessageHandlerMetadata;
+import net.engio.mbassy.listener.MetadataReader;
+import net.engio.mbassy.subscription.Subscription;
+import net.engio.mbassy.subscription.SubscriptionFactory;
 
 import java.util.*;
 import java.util.concurrent.*;
-import java.util.concurrent.atomic.AtomicBoolean;
 
 /**
  * The base class for all message bus implementations.
```
#### Possible refactoring

| **Refactoring Type**         | **Manifestation in This Change** |
|-----------------------------|----------------------------------|
| **Move Package**   | `org.mbassy` → `net.engio.mbassy` |
| **Move Class**     | `AbstractMessageBus.java` migrated to a new path |



### Different paths, different class names

| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | ce80e8b | 100 | Move Method | private_int_getNumberOfSubscribedListeners' from 'src/test/java/org/mbassy/MBassadorTest' to 'src/test/java/net/engio/mbassy/ListenerSubscriptionTest' | src/test/java/org/mbassy/MBassadorTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava | src/test/java/net/engio/mbassy/ListenerSubscriptionTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava |


#### tokenized log
```
====== DIFF: a/src/test/java/org/mbassy/MBassadorTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava ======
diff --git a/src/test/java/org/mbassy/MBassadorTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava b/src/test/java/net/engio/mbassy/ListenerSubscriptionTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava
similarity index 100%
rename from src/test/java/org/mbassy/MBassadorTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava
rename to src/test/java/net/engio/mbassy/ListenerSubscriptionTest#private_int_getNumberOfSubscribedListeners(Collection[Subscription]).mjava
```
  

#### original log

<details>
<summary>Associated Modifications</summary>

```
====== DIFF: a/src/test/java/org/mbassy/AllTests.java ======
diff --git a/src/test/java/org/mbassy/AllTests.java b/src/test/java/net/engio/mbassy/AllTests.java
similarity index 69%
rename from src/test/java/org/mbassy/AllTests.java
rename to src/test/java/net/engio/mbassy/AllTests.java
index 69ea305..9e85111 100644
--- a/src/test/java/org/mbassy/AllTests.java
+++ b/src/test/java/net/engio/mbassy/AllTests.java
@@ -1,4 +1,4 @@
-package org.mbassy;
+package net.engio.mbassy;
 
 import org.junit.runner.RunWith;
 import org.junit.runners.Suite;
@@ -12,9 +12,10 @@ import org.junit.runners.Suite;
 @RunWith(Suite.class)
 @Suite.SuiteClasses({
         ConcurrentSetTest.class,
-        MBassadorTest.class,
+        MessagePublicationTest.class,
         FilterTest.class,
-        MetadataReaderTest.class
+        MetadataReaderTest.class,
+        ListenerSubscriptionTest.class
 })
 public class AllTests {
 }
``` 
</details>

---
<details>
<summary>src/test/java/org/mbassy/MBassadorTest</summary>

```
====== DIFF: a/src/test/java/org/mbassy/MBassadorTest.java ======
diff --git a/src/test/java/org/mbassy/MBassadorTest.java b/src/test/java/org/mbassy/MBassadorTest.java
deleted file mode 100644
index d15bd3e..0000000
--- a/src/test/java/org/mbassy/MBassadorTest.java
+++ /dev/null
@@ -1,221 +0,0 @@
-package org.mbassy;
-
-import java.util.Collection;
-import java.util.LinkedList;
-import java.util.List;
-import java.util.concurrent.CopyOnWriteArrayList;
-
-import org.junit.Test;
-import org.mbassy.events.SubTestEvent;
-import org.mbassy.events.TestEvent;
-import org.mbassy.events.TestEvent2;
-import org.mbassy.listeners.EventingTestBean;
-import org.mbassy.listeners.EventingTestBean2;
-import org.mbassy.listeners.EventingTestBean3;
-import org.mbassy.listeners.ListenerFactory;
-import org.mbassy.listeners.MultiEventHandler;
-import org.mbassy.listeners.NonListeningBean;
-import org.mbassy.subscription.Subscription;
-
-/**
- * Test synchronous and asynchronous dispatch in single and multi-threaded scenario.
- *
- * @author bennidi
- *         Date: 2/8/12
- */
-public class MBassadorTest extends UnitTest {
-
-
-    // this is a single threaded test for subscribing and unsubscribing of a single listener
-    @Test
-    public void testSubscribeSimple() throws InterruptedException {
-        MBassador bus = new MBassador(new BusConfiguration());
-        List<Object> listeners = new LinkedList<Object>();
-        int listenerCount = 1000;
-
-        // subscribe a number of listeners to the bus
-        for (int i = 1; i <= listenerCount; i++) {
-            EventingTestBean listener = new EventingTestBean();
-            NonListeningBean nonListener = new NonListeningBean();
-            listeners.add(listener);
-
-            bus.subscribe(listener);
-            bus.subscribe(nonListener);
-
-            assertFalse(bus.unsubscribe(nonListener)); // these are not expected to be subscribed listeners
-            assertFalse(bus.unsubscribe(new EventingTestBean()));
-
-        }
-
-        // check the generated subscriptions for existence of all previously subscribed valid listeners
-        Collection<Subscription> testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
-        assertEquals(1, testEventsubscriptions.size());
-        assertEquals(listenerCount, getNumberOfSubscribedListeners(testEventsubscriptions));
-
-        Collection<Subscription> subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
-        assertEquals(3, subTestEventsubscriptions.size());
-        assertEquals(3 * listenerCount, getNumberOfSubscribedListeners(subTestEventsubscriptions));
-
-        // unsubscribe the listeners
-        for(Object listener : listeners){
-            assertTrue(bus.unsubscribe(listener)); // this listener is expected to exist
-        }
-
-        // no listener should be left
-        testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
-        assertEquals(1, testEventsubscriptions.size());
-        assertEquals(0, getNumberOfSubscribedListeners(testEventsubscriptions));
-
-        subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
-        assertEquals(3, subTestEventsubscriptions.size());
-        assertEquals(0, getNumberOfSubscribedListeners(subTestEventsubscriptions));
-
-    }
-
-    private int getNumberOfSubscribedListeners(Collection<Subscription> subscriptions) {
-        int listeners = 0;
-        for (Subscription sub : subscriptions) {
-            listeners += sub.size();
-        }
-        return listeners;
-    }
-
-    @Test
-    public void testConcurrentSubscription() throws Exception {
-
-        MBassador bus = new MBassador(new BusConfiguration());
-        ListenerFactory listenerFactory = new ListenerFactory()
-                .create(100, EventingTestBean.class)
-                .create(100, EventingTestBean2.class)
-                .create(100, EventingTestBean3.class)
-                .create(100, Object.class)
-                .create(100, NonListeningBean.class);
-
-        List<Object> listeners = listenerFactory.build();
-
-        // this will subscribe the listeners concurrently to the bus
-        TestUtil.setup(bus, listeners, 10);
-
-        // check the generated subscriptions for existence of all previously subscribed valid listeners
-        Collection<Subscription> testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
-        assertEquals(3, testEventsubscriptions.size());
-        assertEquals(300, getNumberOfSubscribedListeners(testEventsubscriptions));
-
-        Collection<Subscription> subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
-        assertEquals(10, subTestEventsubscriptions.size());
-        assertEquals(1000, getNumberOfSubscribedListeners(subTestEventsubscriptions));
-
-    }
-
-
-    @Test
-    public void testAsynchronousMessagePublication() throws Exception {
-
-        MBassador bus = new MBassador(new BusConfiguration());
-        ListenerFactory listenerFactory = new ListenerFactory()
-                .create(100, EventingTestBean.class)
-                .create(100, EventingTestBean2.class)
-                .create(100, EventingTestBean3.class)
-                .create(100, Object.class)
-                .create(100, NonListeningBean.class)
-                .create(100, MultiEventHandler.class);
-
-        List<Object> listeners = listenerFactory.build();
-
-        // this will subscribe the listeners concurrently to the bus
-        TestUtil.setup(bus, listeners, 10);
-
-        TestEvent event = new TestEvent();
-        TestEvent subEvent = new SubTestEvent();
-        TestEvent2 event2 = new TestEvent2();
-
-        bus.publishAsync(event);
-        bus.publishAsync(subEvent);
-        bus.publishAsync(event2);
-
-        pause(2000);
-
-        assertEquals(500, event.counter.get());
-        assertEquals(800, subEvent.counter.get());
-        assertEquals(200, event2.counter.get());
-
-    }
-
-    @Test
-    public void testSynchronousMessagePublication() throws Exception {
-
-        MBassador bus = new MBassador(new BusConfiguration());
-        ListenerFactory listenerFactory = new ListenerFactory()
-                .create(100, EventingTestBean.class)
-                .create(100, EventingTestBean2.class)
-                .create(100, EventingTestBean3.class)
-                .create(100, Object.class)
-                .create(100, NonListeningBean.class);
-
-        List<Object> listeners = listenerFactory.build();
-
-        // this will subscribe the listeners concurrently to the bus
-        TestUtil.setup(bus, listeners, 10);
-
-        TestEvent event = new TestEvent();
-        TestEvent subEvent = new SubTestEvent();
-
-        bus.publish(event);
-        bus.publish(subEvent);
-
-        pause(2000);
-
-        assertEquals(300, event.counter.get());
-        assertEquals(700, subEvent.counter.get());
-
-    }
-
-    @Test
-    public void testConcurrentMixedMessagePublication() throws Exception {
-        final CopyOnWriteArrayList<TestEvent> testEvents = new CopyOnWriteArrayList<TestEvent>();
-        final CopyOnWriteArrayList<SubTestEvent> subtestEvents = new CopyOnWriteArrayList<SubTestEvent>();
-        final int eventLoopsPerTHread = 100;
-
-
-        final MBassador bus = new MBassador(new BusConfiguration());
-        ListenerFactory listenerFactory = new ListenerFactory()
-                .create(100, EventingTestBean.class)
-                .create(100, EventingTestBean2.class)
-                .create(100, EventingTestBean3.class)
-                .create(100, Object.class)
-                .create(100, NonListeningBean.class);
-
-        List<Object> listeners = listenerFactory.build();
-
-        // this will subscribe the listeners concurrently to the bus
-        TestUtil.setup(bus, listeners, 10);
-
-        ConcurrentExecutor.runConcurrent(new Runnable() {
-            @Override
-            public void run() {
-                for (int i = 0; i < eventLoopsPerTHread; i++) {
-                    TestEvent event = new TestEvent();
-                    SubTestEvent subEvent = new SubTestEvent();
-                    testEvents.add(event);
-                    subtestEvents.add(subEvent);
-
-                    bus.publishAsync(event);
-                    bus.publish(subEvent);
-                }
-            }
-        }, 10);
-
-        pause(3000);
-
-        for (TestEvent event : testEvents) {
-            assertEquals(300, event.counter.get());
-        }
-
-        for (SubTestEvent event : subtestEvents) {
-            assertEquals(700, event.counter.get());
-        }
-
-    }
-
-
-}
```
</details>

---

<details>
<summary>src/test/java/net/engio/mbassy/ListenerSubscriptionTest</summary>
  
```
====== DIFF: a/src/test/java/net/engio/mbassy/ListenerSubscriptionTest.java ======
diff --git a/src/test/java/net/engio/mbassy/ListenerSubscriptionTest.java b/src/test/java/net/engio/mbassy/ListenerSubscriptionTest.java
new file mode 100644
index 0000000..815c989
--- /dev/null
+++ b/src/test/java/net/engio/mbassy/ListenerSubscriptionTest.java
@@ -0,0 +1,104 @@
+package net.engio.mbassy;
+
+import org.junit.Test;
+import net.engio.mbassy.common.TestUtil;
+import net.engio.mbassy.common.UnitTest;
+import net.engio.mbassy.events.SubTestEvent;
+import net.engio.mbassy.events.TestEvent;
+import net.engio.mbassy.listeners.*;
+import net.engio.mbassy.subscription.Subscription;
+
+import java.util.Collection;
+import java.util.LinkedList;
+import java.util.List;
+
+/**
+ * Testing different scenarios of subscribing objects (listeners and non-listeners) to the message bus.
+ *
+ * @author bennidi
+ *         Date: 1/9/13
+ */
+public class ListenerSubscriptionTest extends UnitTest{
+
+
+    // this is a single threaded test for subscribing and unsubscribing of a single listener
+    @Test
+    public void testSubscribeSimple() throws InterruptedException {
+        MBassador bus = new MBassador(new BusConfiguration());
+        List<Object> listeners = new LinkedList<Object>();
+        int listenerCount = 200000;
+
+        // subscribe a number of listeners to the bus
+        for (int i = 1; i <= listenerCount; i++) {
+            EventingTestBean listener = new EventingTestBean();
+            NonListeningBean nonListener = new NonListeningBean();
+            listeners.add(listener);
+
+            bus.subscribe(listener);
+            bus.subscribe(nonListener);
+
+            assertFalse(bus.unsubscribe(nonListener)); // these are not expected to be subscribed listeners
+            assertFalse(bus.unsubscribe(new EventingTestBean()));
+
+        }
+
+        // check the generated subscriptions for existence of all previously subscribed valid listeners
+        Collection<Subscription> testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
+        assertEquals(1, testEventsubscriptions.size());
+        assertEquals(listenerCount, getNumberOfSubscribedListeners(testEventsubscriptions));
+
+        Collection<Subscription> subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
+        assertEquals(3, subTestEventsubscriptions.size());
+        assertEquals(3 * listenerCount, getNumberOfSubscribedListeners(subTestEventsubscriptions));
+
+        // unsubscribe the listeners
+        for(Object listener : listeners){
+            assertTrue(bus.unsubscribe(listener)); // this listener is expected to exist
+        }
+
+        // no listener should be left
+        testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
+        assertEquals(1, testEventsubscriptions.size());
+        assertEquals(0, getNumberOfSubscribedListeners(testEventsubscriptions));
+
+        subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
+        assertEquals(3, subTestEventsubscriptions.size());
+        assertEquals(0, getNumberOfSubscribedListeners(subTestEventsubscriptions));
+
+    }
+
+    private int getNumberOfSubscribedListeners(Collection<Subscription> subscriptions) {
+        int listeners = 0;
+        for (Subscription sub : subscriptions) {
+            listeners += sub.size();
+        }
+        return listeners;
+    }
+
+    @Test
+    public void testConcurrentSubscription() throws Exception {
+
+        MBassador bus = new MBassador(new BusConfiguration());
+        ListenerFactory listenerFactory = new ListenerFactory()
+                .create(10000, EventingTestBean.class)
+                .create(10000, EventingTestBean2.class)
+                .create(10000, EventingTestBean3.class)
+                .create(10000, Object.class)
+                .create(10000, NonListeningBean.class);
+
+        List<Object> listeners = listenerFactory.build();
+
+        // this will subscribe the listeners concurrently to the bus
+        TestUtil.setup(bus, listeners, 10);
+
+        // check the generated subscriptions for existence of all previously subscribed valid listeners
+        Collection<Subscription> testEventsubscriptions = bus.getSubscriptionsByMessageType(TestEvent.class);
+        assertEquals(3, testEventsubscriptions.size());
+        assertEquals(30000, getNumberOfSubscribedListeners(testEventsubscriptions));
+
+        Collection<Subscription> subTestEventsubscriptions = bus.getSubscriptionsByMessageType(SubTestEvent.class);
+        assertEquals(10, subTestEventsubscriptions.size());
+        assertEquals(100000, getNumberOfSubscribedListeners(subTestEventsubscriptions));
+
+    }
+}
```
</details> 

<details>
<summary>src/test/java/net/engio/mbassy/MessagePublicationTest</summary>
  
```
====== DIFF: a/src/test/java/net/engio/mbassy/MessagePublicationTest.java ======
diff --git a/src/test/java/net/engio/mbassy/MessagePublicationTest.java b/src/test/java/net/engio/mbassy/MessagePublicationTest.java
new file mode 100644
index 0000000..22fb1da
--- /dev/null
+++ b/src/test/java/net/engio/mbassy/MessagePublicationTest.java
@@ -0,0 +1,144 @@
+package net.engio.mbassy;
+
+import java.util.List;
+import java.util.concurrent.CopyOnWriteArrayList;
+
+import org.junit.Test;
+import net.engio.mbassy.common.ConcurrentExecutor;
+import net.engio.mbassy.common.TestUtil;
+import net.engio.mbassy.common.UnitTest;
+import net.engio.mbassy.events.SubTestEvent;
+import net.engio.mbassy.events.TestEvent;
+import net.engio.mbassy.events.TestEvent2;
+import net.engio.mbassy.listeners.EventingTestBean;
+import net.engio.mbassy.listeners.EventingTestBean2;
+import net.engio.mbassy.listeners.EventingTestBean3;
+import net.engio.mbassy.listeners.ListenerFactory;
+import net.engio.mbassy.listeners.MultiEventHandler;
+import net.engio.mbassy.listeners.NonListeningBean;
+
+/**
+ * Test synchronous and asynchronous dispatch in single and multi-threaded scenario.
+ *
+ * @author bennidi
+ *         Date: 2/8/12
+ */
+public class MessagePublicationTest extends UnitTest {
+
+    // this value probably needs to be adjusted depending on the performance of the underlying plattform
+    // otherwise the tests will fail since asynchronous processing might not have finished when
+    // evaluation is run
+    private int processingTimeInMS = 4000;
+
+
+    @Test
+    public void testAsynchronousMessagePublication() throws Exception {
+
+        MBassador bus = new MBassador(new BusConfiguration());
+        ListenerFactory listenerFactory = new ListenerFactory()
+                .create(10000, EventingTestBean.class)
+                .create(10000, EventingTestBean2.class)
+                .create(10000, EventingTestBean3.class)
+                .create(10000, Object.class)
+                .create(10000, NonListeningBean.class)
+                .create(10000, MultiEventHandler.class);
+
+        List<Object> listeners = listenerFactory.build();
+
+        // this will subscribe the listeners concurrently to the bus
+        TestUtil.setup(bus, listeners, 10);
+
+        TestEvent event = new TestEvent();
+        TestEvent subEvent = new SubTestEvent();
+        TestEvent2 event2 = new TestEvent2();
+
+        bus.publishAsync(event);
+        bus.publishAsync(subEvent);
+        bus.publishAsync(event2);
+
+        pause(processingTimeInMS);
+
+        assertEquals(50000, event.counter.get());
+        assertEquals(80000, subEvent.counter.get());
+        assertEquals(20000, event2.counter.get());
+
+    }
+
+    @Test
+    public void testSynchronousMessagePublication() throws Exception {
+
+        MBassador bus = new MBassador(new BusConfiguration());
+        ListenerFactory listenerFactory = new ListenerFactory()
+                .create(10000, EventingTestBean.class)
+                .create(10000, EventingTestBean2.class)
+                .create(10000, EventingTestBean3.class)
+                .create(10000, Object.class)
+                .create(10000, NonListeningBean.class);
+
+        List<Object> listeners = listenerFactory.build();
+
+        // this will subscribe the listeners concurrently to the bus
+        TestUtil.setup(bus, listeners, 10);
+
+        TestEvent event = new TestEvent();
+        TestEvent subEvent = new SubTestEvent();
+
+        bus.publish(event);
+        bus.publish(subEvent);
+
+        pause(processingTimeInMS);
+
+        assertEquals(30000, event.counter.get());
+        assertEquals(70000, subEvent.counter.get());
+
+    }
+
+    @Test
+    public void testConcurrentMixedMessagePublication() throws Exception {
+        final CopyOnWriteArrayList<TestEvent> testEvents = new CopyOnWriteArrayList<TestEvent>();
+        final CopyOnWriteArrayList<SubTestEvent> subtestEvents = new CopyOnWriteArrayList<SubTestEvent>();
+        final int eventLoopsPerTHread = 100;
+
+
+        final MBassador bus = new MBassador(new BusConfiguration());
+        ListenerFactory listenerFactory = new ListenerFactory()
+                .create(10000, EventingTestBean.class)
+                .create(10000, EventingTestBean2.class)
+                .create(10000, EventingTestBean3.class)
+                .create(10000, Object.class)
+                .create(10000, NonListeningBean.class);
+
+        List<Object> listeners = listenerFactory.build();
+
+        // this will subscribe the listeners concurrently to the bus
+        TestUtil.setup(bus, listeners, 10);
+
+        ConcurrentExecutor.runConcurrent(new Runnable() {
+            @Override
+            public void run() {
+                for (int i = 0; i < eventLoopsPerTHread; i++) {
+                    TestEvent event = new TestEvent();
+                    SubTestEvent subEvent = new SubTestEvent();
+                    testEvents.add(event);
+                    subtestEvents.add(subEvent);
+
+                    bus.publishAsync(event);
+                    bus.publish(subEvent);
+                }
+            }
+        }, 10);
+
+        pause(processingTimeInMS);
+
+        for (TestEvent event : testEvents) {
+            assertEquals(30000, event.counter.get());
+        }
+
+        for (SubTestEvent event : subtestEvents) {
+            assertEquals(70000, event.counter.get());
+        }
+
+    }
+
+
+}                                    
```
</details>

#### Possible refactoring
 - Extract Class: Split `MessagePublicationTest` and `ListenerSubscriptionTest` from `MBassadorTest`. 
 - Move Method:

| **Category**                           | **MBassadorTest (Old)** | **MessagePublicationTest (New)** | **ListenerSubscriptionTest (New)** |
|----------------------------------------|------------------------|---------------------------------|----------------------------------|
| **Subscription Test**                  | ✅                     | ❌                              | ✅ (Extracted) |
| **Synchronous Message Publication**    | ✅                     | ✅ (Extracted)                  | ❌                              |
| **Asynchronous Message Publication**   | ✅                     | ✅ (Extracted)                  | ❌                              |
| **Mixed Concurrent Message Publication** | ✅                   | ✅ (Extracted)                  | ❌                              |
| **Class Status**                        | ❌ (Deleted)           | ✅ (New Class)                  | ✅ (New Class)                  |

    
| **Original Method (`MBassadorTest`)**  | **New Location** | **Changes** |
|----------------------------------------|------------------|-------------|
| `testSubscribeSimple()`                | `ListenerSubscriptionTest` | Subscription count increased from 1000 → 200000 |
| `testConcurrentSubscription()`         | `ListenerSubscriptionTest` | Listener instances increased from 100 → 10000 |
| `testAsynchronousMessagePublication()` | `MessagePublicationTest` | Listener instances increased from 100 → 10000, assertion values increased |
| `testSynchronousMessagePublication()`  | `MessagePublicationTest` | Listener instances increased from 100 → 10000 |
| `testConcurrentMixedMessagePublication()` | `MessagePublicationTest` | Listener instances increased from 100 → 10000 |

</details>


<details>
<summary>f8c5bbed910ee0cf16390f32f06f650e0020b1e5</summary>

 - Move method: 17
 - Move and Rename Method: 3

# Move method
 
## Three types 
| Path Change | Class Name Change | Count |
|----------------------------|----------------------------|-------|
| Different paths | Same class name | 8 |
| Different paths | Different class names | 1 |
| Same path | Different class name | 8 |

## Different paths, same class name

## Different paths, different class names

## Same path, different class name

| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|-------------|------------------|--------------|--------------|
| mbassador | f8c5bbe | 100 | Move Method | 'private_Class_getMessageType' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_Class_getMessageType(Method).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_Class_getMessageType(Method).mjava |
| mbassador | f8c5bbe | 100 | Move Method | 'private_Collection[Class]_getSuperclasses' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_Collection[Class]_getSuperclasses(Class).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_Collection[Class]_getSuperclasses(Class).mjava |
| mbassador | f8c5bbe | 100 | Move Method | 'private_List[Method]_getListeners' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_List[Method]_getListeners(Class[#]).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_List[Method]_getListeners(Class[#]).mjava |
| mbassador | f8c5bbe | 100 | Move Method | 'private_boolean_isValidMessageHandler' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_boolean_isValidMessageHandler(Method).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_boolean_isValidMessageHandler(Method).mjava |
| mbassador | f8c5bbe | 100 | Move Method | 'private_void_addMessageTypeSubscription' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_void_addMessageTypeSubscription(Class,Subscription).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava |
| mbassador | f8c5bbe | 100 | Move Method | 'public_void_unsubscribe' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#public_void_unsubscribe(Object).mjava | src/main/java/org/mbassy/AbstractMessageBus#public_void_unsubscribe(Object).mjava |
| mbassador | f8c5bbe | 96 | Move Method | 'private_void_initDispatcherThreads' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_void_initDispatcherThreads(int).mjava | src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava |
| mbassador | f8c5bbe | 91 | Move Method | 'public_void_subscribe' from 'src/main/java/org/mbassy/MBassador' to 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#public_void_subscribe(Object).mjava | src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava |

### without hunks
#### tokenized log

```
====== DIFF: a/src/main/java/org/mbassy/MBassador#private_Class_getMessageType(Method).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_Class_getMessageType(Method).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_Class_getMessageType(Method).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#private_Class_getMessageType(Method).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_Class_getMessageType(Method).mjava

====== DIFF: a/src/main/java/org/mbassy/MBassador#private_Collection[Class]_getSuperclasses(Class).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_Collection[Class]_getSuperclasses(Class).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_Collection[Class]_getSuperclasses(Class).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#private_Collection[Class]_getSuperclasses(Class).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_Collection[Class]_getSuperclasses(Class).mjava

====== DIFF: a/src/main/java/org/mbassy/MBassador#private_List[Method]_getListeners(Class[#]).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_List[Method]_getListeners(Class[#]).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_List[Method]_getListeners(Class[#]).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#private_List[Method]_getListeners(Class[#]).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_List[Method]_getListeners(Class[#]).mjava

====== DIFF: a/src/main/java/org/mbassy/MBassador#private_boolean_isValidMessageHandler(Method).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_boolean_isValidMessageHandler(Method).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_boolean_isValidMessageHandler(Method).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#private_boolean_isValidMessageHandler(Method).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_boolean_isValidMessageHandler(Method).mjava

====== DIFF: a/src/main/java/org/mbassy/MBassador#private_void_addMessageTypeSubscription(Class,Subscription).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_void_addMessageTypeSubscription(Class,Subscription).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#private_void_addMessageTypeSubscription(Class,Subscription).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_void_addMessageTypeSubscription(Class,Subscription).mjava

====== DIFF: a/src/main/java/org/mbassy/MBassador#public_void_unsubscribe(Object).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#public_void_unsubscribe(Object).mjava b/src/main/java/org/mbassy/AbstractMessageBus#public_void_unsubscribe(Object).mjava
similarity index 100%
rename from src/main/java/org/mbassy/MBassador#public_void_unsubscribe(Object).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#public_void_unsubscribe(Object).mjava
```
#### original log

<details>
<summary>src/main/java/org/mbassy/MBassador</summary>

```
====== DIFF: a/src/main/java/org/mbassy/MBassador.java ======
diff --git a/src/main/java/org/mbassy/MBassador.java b/src/main/java/org/mbassy/MBassador.java
index eb5e62e..c9684ff 100644
--- a/src/main/java/org/mbassy/MBassador.java
+++ b/src/main/java/org/mbassy/MBassador.java
@@ -1,102 +1,32 @@
 package org.mbassy;
 
-import org.mbassy.filter.Filter;
-import org.mbassy.filter.MessageFilter;
-import org.mbassy.common.*;
+import org.mbassy.subscription.*;
 
-import java.lang.reflect.InvocationTargetException;
-import java.lang.reflect.Method;
 import java.util.*;
 import java.util.concurrent.*;
 
 
-public class MBassador<T> implements IMessageBus<T, SimplePostCommand>{
-
-
-	//  This predicate is used to find all message listeners (methods annotated with @Listener)
-	private static final IPredicate<Method> AllMessageListeners = new IPredicate<Method>() {
-		@Override
-		public boolean apply(Method target) {
-			return target.getAnnotation(Listener.class) != null;
-		}
-	};
-
-    // This is the default error handler it will simply log to standard out and
-    // print stack trace if available
-	protected static final class ConsoleLogger implements IPublicationErrorHandler {
-		@Override
-		public void handleError(PublicationError error) {
-            System.out.println(error);
-            if (error.getCause() != null) error.getCause().printStackTrace();
-		}
-	};
-
-    // executor for asynchronous listeners using unbound queuing strategy to ensure that no events get lost
-    private ExecutorService executor;
-
-	// cache already created filter instances
-	private final Map<Class<? extends MessageFilter>, MessageFilter> filterCache = new HashMap<Class<? extends MessageFilter>, MessageFilter>();
-
-	// all subscriptions per message type
-	// this is the primary list for dispatching a specific message
-    // write access is synchronized and happens very infrequently
-	private final Map<Class, Collection<Subscription>> subscriptionsPerMessage = new HashMap(50);
-
-	// all subscriptions per messageHandler type
-	// this list provides fast access for subscribing and unsubscribing
-	private final Map<Class, Collection<Subscription>> subscriptionsPerListener = new HashMap(50);
-
-	// remember already processed classes that do not contain any listeners
-	private final Collection<Class> nonListeners = new HashSet();
-
-    // this handler will receive all errors that occur during message dispatch or message handling
-	private IPublicationErrorHandler errorHandler = new ConsoleLogger();
-
-
-    // all threads that are available for asynchronous message dispatching
-    private final CopyOnWriteArrayList<Thread> dispatchers = new CopyOnWriteArrayList<Thread>();
-
-    // all pending messages scheduled for asynchronous dispatch are queued here
-    private final LinkedBlockingQueue<T> pendingMessages = new LinkedBlockingQueue<T>();
-
-    // initialize the dispatch workers
-    private void initDispatcherThreads(int numberOfThreads) {
-        for (int i = 0; i < numberOfThreads; i++) {
-            // each thread will run forever and process incoming
-            //dispatch requests
-            Thread dispatcher = new Thread(new Runnable() {
-                public void run() {
-                    while (true) {
-                        try {
-                            publish(pendingMessages.take());
-                        } catch (InterruptedException e) {
-                            errorHandler.handleError(new PublicationError(e, "Asynchronous publication interrupted", null, null, null));
-                            return;
-                        }
-                    }
-                }
-            });
-            dispatchers.add(dispatcher);
-            dispatcher.start();
-        }
-    }
+public class MBassador<T> extends AbstractMessageBus<T, SimplePostCommand<T>>{
 
     public MBassador(){
         this(2);
     }
 
     public MBassador(int dispatcherThreadCount){
-        this(2, new ThreadPoolExecutor(5, 50, 1, TimeUnit.MINUTES, new LinkedBlockingQueue<Runnable>()));
+        super(dispatcherThreadCount);
     }
 
     public MBassador(int dispatcherThreadCount, ExecutorService executor){
-        this.executor = executor;
-        initDispatcherThreads(dispatcherThreadCount > 0 ? dispatcherThreadCount : 2);
+        super(dispatcherThreadCount,executor);
     }
 
+    @Override
+    protected SubscriptionFactory getSubscriptionFactory() {
+        return new SubscriptionFactory(this);
+    }
 
     public void publishAsync(T message){
-        pendingMessages.offer(message);
+        addAsynchronousDeliveryRequest(new SubscriptionDeliveryRequest<T>(getSubscriptionsByMessageType(message.getClass()), message));
     }
 
 
@@ -125,370 +55,9 @@ public class MBassador<T> implements IMessageBus<T, SimplePostCommand>{
 	}
 
 
-	public void unsubscribe(Object listener){
-		if (listener == null) return;
-		Collection<Subscription> subscriptions = subscriptionsPerListener.get(listener.getClass());
-		if(subscriptions == null)return;
-        for (Subscription subscription : subscriptions) {
-			subscription.unsubscribe(listener);
-		}
-	}
-
     @Override
     public SimplePostCommand post(T message) {
         return new SimplePostCommand(this, message);
     }
 
-    public void subscribe(Object listener){
-		Class listeningClass = listener.getClass();
-		if (nonListeners.contains(listeningClass))
-			return; // early reject of known classes that do not participate in eventing
-		Collection<Subscription> subscriptionsByListener = subscriptionsPerListener.get(listeningClass);
-		if (subscriptionsByListener == null) { // if the type is registered for the first time
-			synchronized (this) { // new subscriptions must be processed sequentially for each class
-				subscriptionsByListener = subscriptionsPerListener.get(listeningClass);
-				if (subscriptionsByListener == null) {  // double check (a bit ugly but works here)
-					List<Method> messageHandlers = getListeners(listeningClass);  // get all methods with subscriptions
-					subscriptionsByListener = new ArrayList<Subscription>(messageHandlers.size()); // it's safe to use non-concurrent collection here (read only)
-					if (messageHandlers.isEmpty()) {  // remember the class as non listening class
-						nonListeners.add(listeningClass);
-						return;
-					}
-					// create subscriptions for all detected listeners
-					for (Method messageHandler : messageHandlers) {
-						if (!isValidMessageHandler(messageHandler)) continue; // ignore invalid listeners
-						MessageFilter[] filter = getFilter(messageHandler.getAnnotation(Listener.class));
-						Class eventType = getMessageType(messageHandler);
-						Subscription subscription = createSubscription(messageHandler, filter);
-						subscription.subscribe(listener);
-						addMessageTypeSubscription(eventType, subscription);
-						subscriptionsByListener.add(subscription);
-						//updateMessageTypeHierarchy(eventType);
-					}
-					subscriptionsPerListener.put(listeningClass, subscriptionsByListener);
-				}
-			}
-		}
-		// register the listener to the existing subscriptions
-		for (Subscription sub : subscriptionsByListener) sub.subscribe(listener);
-	}
-
-
-	public void setErrorHandler(IPublicationErrorHandler handler){
-		this.errorHandler = handler;
-	}
-
-
-
-	// obtain the set of subscriptions for the given message type
-	private Collection<Subscription> getSubscriptionsByMessageType(Class messageType) {
-		List<Subscription> subscriptions = new LinkedList<Subscription>();
-
-		if(subscriptionsPerMessage.get(messageType) != null) {
-			subscriptions.addAll(subscriptionsPerMessage.get(messageType));
-		}
-		for (Class eventSuperType : getSuperclasses(messageType)){
-           if(subscriptionsPerMessage.get(eventSuperType) != null){
-               subscriptions.addAll(subscriptionsPerMessage.get(eventSuperType));
-           }
-        }
-        // IMPROVEMENT: use tree list that sorts during insertion
-		//Collections.sort(subscriptions, new SubscriptionByPriorityDesc());
-        return subscriptions;
-	}
-
-    private Collection<Class> getSuperclasses(Class from){
-        Collection<Class> superclasses = new LinkedList<Class>();
-        while(!from.equals(Object.class)){
-            superclasses.add(from.getSuperclass());
-            from = from.getSuperclass();
-        }
-        return superclasses;
-    }
-
-	// associate a suscription with a message type
-	private void addMessageTypeSubscription(Class messageType, Subscription subscription) {
-		Collection<Subscription> subscriptions = subscriptionsPerMessage.get(messageType);
-		if (subscriptions == null) {
-			subscriptions = new CopyOnWriteArraySet<Subscription>();
-			subscriptionsPerMessage.put(messageType, subscriptions);
-		}
-		subscriptions.add(subscription);
-	}
-
-
-	private boolean isValidMessageHandler(Method handler) {
-		if (handler.getParameterTypes().length != 1) {
-			// a messageHandler only defines one parameter (the message)
-			System.out.println("Found no or more than one parameter in messageHandler [" + handler.getName()
-					+ "]. A messageHandler must define exactly one parameter");
-			return false;
-		}
-		return true;
-	}
-
-	private static Class getMessageType(Method listener) {
-		return listener.getParameterTypes()[0];
-	}
-
-	// get all listeners defined by the given class (includes
-	// listeners defined in super classes)
-	private static List<Method> getListeners(Class<?> target) {
-		return ReflectionUtils.getMethods(AllMessageListeners, target);
-	}
-
-	// retrieve all instances of filters associated with the given subscription
-	private MessageFilter[] getFilter(Listener subscription) {
-		if (subscription.value().length == 0) return null;
-		MessageFilter[] filters = new MessageFilter[subscription.value().length];
-		int i = 0;
-		for (Filter filterDef : subscription.value()) {
-			MessageFilter filter = filterCache.get(filterDef.value());
-			if (filter == null) {
-				try {
-					filter = filterDef.value().newInstance();
-					filterCache.put(filterDef.value(), filter);
-				} catch (Throwable e) {
-					handlePublicationError(new PublicationError()
-							.setMessage("Error retrieving filter"));
-				}
-
-			}
-			filters[i] = filter;
-			i++;
-		}
-		return filters;
-	}
-
-
-
-	private void handlePublicationError(PublicationError error) {
-		errorHandler.handleError(error);
-	}
-
-    @Override
-    protected void finalize() throws Throwable {
-        super.finalize();
-        for(Thread dispatcher : dispatchers){
-            dispatcher.interrupt();
-        }
-    }
-
-
-    private Subscription createSubscription(Method messageHandler, MessageFilter[] filter){
-        if(filter == null || filter.length == 0){
-            if(isAsynchronous(messageHandler)){
-                return new UnfilteredAsynchronousSubscription(messageHandler);
-            }
-            else{
-                return new UnfilteredSynchronousSubscription(messageHandler);
-            }
-        }
-        else{
-            if(isAsynchronous(messageHandler)){
-                return new FilteredAsynchronousSubscription(messageHandler, filter);
-            }
-            else{
-                return new FilteredSynchronousSubscription(messageHandler, filter);
-            }
-        }
-    }
-
-    private boolean isAsynchronous(Method messageHandler){
-         return messageHandler.getAnnotation(Listener.class).mode().equals(Listener.Dispatch.Asynchronous);
-    }
-
-
-    /**
-     * Subscription is a thread safe container for objects that contain message handlers
-     */
-	private abstract class Subscription {
-
-		private final Method messageHandler;
-
-		protected ConcurrentSet<Object> listeners = new ConcurrentSet<Object>();
-
-        private int priority = 0;
-
-		private Subscription(Method messageHandler) {
-            // TODO: init priority
-			this.messageHandler = messageHandler;
-            this.messageHandler.setAccessible(true);
-		}
-
-        protected abstract void publish(Object message);
-
-        protected abstract void dispatch(final Object message, final Object listener);
-
-
-        public int getPriority(){
-            return priority;
-        }
-
-
-		public void subscribe(Object o) {
-			listeners.add(o);
-
-		}
-
-        protected void invokeHandler(final Object message, final Object listener){
-            try {
-                messageHandler.invoke(listener, message);
-            }catch(IllegalAccessException e){
-                MBassador.this.handlePublicationError(
-                        new PublicationError(e, "Error during messageHandler notification. " +
-                                "The class or method is not accessible",
-                                messageHandler, listener, message));
-            }
-            catch(IllegalArgumentException e){
-                MBassador.this.handlePublicationError(
-                        new PublicationError(e, "Error during messageHandler notification. " +
-                                "Wrong arguments passed to method. Was: " + message.getClass()
-                                + "Expected: " + messageHandler.getParameterTypes()[0],
-                                messageHandler, listener, message));
-            }
-            catch (InvocationTargetException e) {
-                MBassador.this.handlePublicationError(
-                        new PublicationError(e, "Error during messageHandler notification. " +
-                                "Message handler threw exception",
-                                messageHandler, listener, message));
-            }
-            catch (Throwable e) {
-                MBassador.this.handlePublicationError(
-                        new PublicationError(e, "Error during messageHandler notification. " +
-                                "Unexpected exception",
-                                messageHandler, listener, message));
-            }
-        }
-
-
-		public void unsubscribe(Object existingListener) {
-			listeners.remove(existingListener);
-		}
-
-
-
-
-	}
-
-    private abstract class UnfilteredSubscription extends Subscription{
-
-
-        private UnfilteredSubscription(Method messageHandler) {
-            super(messageHandler);
-        }
-
-        public void publish(Object message) {
-
-            Iterator<Object> iterator = listeners.iterator();
-            Object listener = null;
-            while ((listener = iterator.next()) != null) {
-                dispatch(message, listener);
-            }
-        }
-    }
-
-    private class UnfilteredAsynchronousSubscription extends UnfilteredSubscription{
-
-
-        private UnfilteredAsynchronousSubscription(Method messageHandler) {
-            super(messageHandler);
-        }
-
-        protected void dispatch(final Object message, final Object listener){
-                MBassador.this.executor.execute(new Runnable() {
-                    @Override
-                    public void run() {
-                        invokeHandler(message, listener);
-                    }
-                });
-
-        }
-    }
-
-    private class UnfilteredSynchronousSubscription extends UnfilteredSubscription{
-
-
-        private UnfilteredSynchronousSubscription(Method messageHandler) {
-            super(messageHandler);
-        }
-
-        protected void dispatch(final Object message, final Object listener){
-            invokeHandler(message, listener);
-        }
-    }
-
-    private abstract class FilteredSubscription extends Subscription{
-
-        private final MessageFilter[] filter;
-
-
-        private FilteredSubscription(Method messageHandler, MessageFilter[] filter) {
-            super(messageHandler);
-            this.filter = filter;
-        }
-
-        private boolean passesFilter(Object message, Object listener) {
-
-            if (filter == null) {
-                return true;
-            }
-            else {
-                for (int i = 0; i < filter.length; i++) {
-                    if (!filter[i].accepts(message, listener)) return false;
-                }
-                return true;
-            }
-        }
-
-        protected void publish(Object message) {
-
-            Iterator<Object> iterator = listeners.iterator();
-            Object listener = null;
-            while ((listener = iterator.next()) != null) {
-                if(passesFilter(message, listener)) {
-                    dispatch(message, listener);
-                }
-            }
-        }
-    }
-
-    private class FilteredSynchronousSubscription extends FilteredSubscription{
-
-
-        private FilteredSynchronousSubscription(Method messageHandler, MessageFilter[] filter) {
-            super(messageHandler, filter);
-        }
-
-        protected void dispatch(final Object message, final Object listener){
-            MBassador.this.executor.execute(new Runnable() {
-                @Override
-                public void run() {
-                    invokeHandler(message, listener);
-                }
-            });
-
-        }
-    }
-
-    private class FilteredAsynchronousSubscription extends FilteredSubscription{
-
-
-        private FilteredAsynchronousSubscription(Method messageHandler, MessageFilter[] filter) {
-            super(messageHandler, filter);
-        }
-
-        protected void dispatch(final Object message, final Object listener){
-            invokeHandler(message, listener);
-        }
-    }
-
-
-    private final class SubscriptionByPriorityDesc implements Comparator<Subscription> {
-        @Override
-        public int compare(Subscription o1, Subscription o2) {
-            return o1.getPriority() - o2.getPriority();
-        }
-    };
-
 }
```
</details>

<details>
<summary>src/main/java/org/mbassy/AbstractMessageBus</summary>

```
====== DIFF: a/src/main/java/org/mbassy/AbstractMessageBus.java ======
diff --git a/src/main/java/org/mbassy/AbstractMessageBus.java b/src/main/java/org/mbassy/AbstractMessageBus.java
new file mode 100644
index 0000000..9747408
--- /dev/null
+++ b/src/main/java/org/mbassy/AbstractMessageBus.java
@@ -0,0 +1,247 @@
+package org.mbassy;
+
+import org.mbassy.common.IPredicate;
+import org.mbassy.common.ReflectionUtils;
+import org.mbassy.listener.Listener;
+import org.mbassy.listener.MetadataReader;
+import org.mbassy.subscription.Subscription;
+import org.mbassy.subscription.SubscriptionDeliveryRequest;
+import org.mbassy.subscription.SubscriptionFactory;
+
+import java.lang.reflect.Method;
+import java.util.*;
+import java.util.concurrent.*;
+
+
+public abstract class AbstractMessageBus<T, P extends IMessageBus.IPostCommand> implements IMessageBus<T, P> {
+
+
+    //  This predicate is used to find all message listeners (methods annotated with @Listener)
+    private static final IPredicate<Method> AllMessageListeners = new IPredicate<Method>() {
+        @Override
+        public boolean apply(Method target) {
+            return target.getAnnotation(Listener.class) != null;
+        }
+    };
+
+    // This is the default error handler it will simply log to standard out and
+    // print stack trace if available
+    protected static final class ConsoleLogger implements IPublicationErrorHandler {
+        @Override
+        public void handleError(PublicationError error) {
+            System.out.println(error);
+            if (error.getCause() != null) error.getCause().printStackTrace();
+        }
+    }
+
+    ;
+
+    // executor for asynchronous listeners using unbound queuing strategy to ensure that no events get lost
+    private ExecutorService executor;
+
+    private MetadataReader metadataReader = new MetadataReader();
+
+    // all subscriptions per message type
+    // this is the primary list for dispatching a specific message
+    // write access is synchronized and happens very infrequently
+    private final Map<Class, Collection<Subscription>> subscriptionsPerMessage = new HashMap(50);
+
+    // all subscriptions per messageHandler type
+    // this list provides fast access for subscribing and unsubscribing
+    // write access is synchronized and happens very infrequently
+    private final Map<Class, Collection<Subscription>> subscriptionsPerListener = new HashMap(50);
+
+    // remember already processed classes that do not contain any listeners
+    private final Collection<Class> nonListeners = new HashSet();
+
+    // this handler will receive all errors that occur during message dispatch or message handling
+    private CopyOnWriteArrayList<IPublicationErrorHandler> errorHandlers = new CopyOnWriteArrayList<IPublicationErrorHandler>();
+
+    // all threads that are available for asynchronous message dispatching
+    private final CopyOnWriteArrayList<Thread> dispatchers = new CopyOnWriteArrayList<Thread>();
+
+    // all pending messages scheduled for asynchronous dispatch are queued here
+    private final LinkedBlockingQueue<SubscriptionDeliveryRequest<T>> pendingMessages = new LinkedBlockingQueue<SubscriptionDeliveryRequest<T>>();
+
+    private final SubscriptionFactory subscriptionFactory;
+
+    // initialize the dispatch workers
+    private void initDispatcherThreads(int numberOfThreads) {
+        for (int i = 0; i < numberOfThreads; i++) {
+            // each thread will run forever and process incoming
+            //dispatch requests
+            Thread dispatcher = new Thread(new Runnable() {
+                public void run() {
+                    while (true) {
+                        try {
+                           pendingMessages.take().execute();
+                        } catch (InterruptedException e) {
+                            handlePublicationError(new PublicationError(e, "Asynchronous publication interrupted", null, null, null));
+                            return;
+                        }
+                    }
+                }
+            });
+            dispatchers.add(dispatcher);
+            dispatcher.start();
+        }
+    }
+
+    public AbstractMessageBus() {
+        this(2);
+    }
+
+    public AbstractMessageBus(int dispatcherThreadCount) {
+        this(2, new ThreadPoolExecutor(5, 50, 1, TimeUnit.MINUTES, new LinkedBlockingQueue<Runnable>()));
+    }
+
+    public AbstractMessageBus(int dispatcherThreadCount, ExecutorService executor) {
+        this.executor = executor;
+        initDispatcherThreads(dispatcherThreadCount > 0 ? dispatcherThreadCount : 2);
+        addErrorHandler(new ConsoleLogger());
+        subscriptionFactory = getSubscriptionFactory();
+        initialize();
+    }
+
+    protected abstract SubscriptionFactory getSubscriptionFactory();
+
+    protected void initialize(){}
+
+    @Override
+    public Collection<IPublicationErrorHandler> getRegisteredErrorHandlers() {
+        return Collections.unmodifiableCollection(errorHandlers);
+    }
+
+    public void unsubscribe(Object listener) {
+        if (listener == null) return;
+        Collection<Subscription> subscriptions = subscriptionsPerListener.get(listener.getClass());
+        if (subscriptions == null) return;
+        for (Subscription subscription : subscriptions) {
+            subscription.unsubscribe(listener);
+        }
+    }
+
+
+    public void subscribe(Object listener) {
+        try {
+            Class listeningClass = listener.getClass();
+            if (nonListeners.contains(listeningClass))
+                return; // early reject of known classes that do not participate in eventing
+            Collection<Subscription> subscriptionsByListener = subscriptionsPerListener.get(listeningClass);
+            if (subscriptionsByListener == null) { // if the type is registered for the first time
+                synchronized (this) { // new subscriptions must be processed sequentially for each class
+                    subscriptionsByListener = subscriptionsPerListener.get(listeningClass);
+                    if (subscriptionsByListener == null) {  // double check (a bit ugly but works here)
+                        List<Method> messageHandlers = getListeners(listeningClass);  // get all methods with subscriptions
+                        subscriptionsByListener = new ArrayList<Subscription>(messageHandlers.size()); // it's safe to use non-concurrent collection here (read only)
+                        if (messageHandlers.isEmpty()) {  // remember the class as non listening class
+                            nonListeners.add(listeningClass);
+                            return;
+                        }
+                        // create subscriptions for all detected listeners
+                        for (Method messageHandler : messageHandlers) {
+                            if (!isValidMessageHandler(messageHandler)) continue; // ignore invalid listeners
+                            Class eventType = getMessageType(messageHandler);
+                            Subscription subscription = subscriptionFactory.createSubscription(metadataReader.getHandlerMetadata(messageHandler));
+                            subscription.subscribe(listener);
+                            addMessageTypeSubscription(eventType, subscription);
+                            subscriptionsByListener.add(subscription);
+                            //updateMessageTypeHierarchy(eventType);
+                        }
+                        subscriptionsPerListener.put(listeningClass, subscriptionsByListener);
+                    }
+                }
+            }
+            // register the listener to the existing subscriptions
+            for (Subscription sub : subscriptionsByListener) sub.subscribe(listener);
+        } catch (Exception e) {
+            throw new RuntimeException(e);
+        }
+    }
+
+
+    public void addErrorHandler(IPublicationErrorHandler handler) {
+        errorHandlers.add(handler);
+    }
+
+    protected void addAsynchronousDeliveryRequest(SubscriptionDeliveryRequest<T> request) {
+        pendingMessages.offer(request);
+    }
+
+    // obtain the set of subscriptions for the given message type
+    protected Collection<Subscription> getSubscriptionsByMessageType(Class messageType) {
+        Set<Subscription> subscriptions = new TreeSet<Subscription>(Subscription.SubscriptionByPriorityDesc);
+
+        if (subscriptionsPerMessage.get(messageType) != null) {
+            subscriptions.addAll(subscriptionsPerMessage.get(messageType));
+        }
+        for (Class eventSuperType : getSuperclasses(messageType)) {
+            if (subscriptionsPerMessage.get(eventSuperType) != null) {
+                subscriptions.addAll(subscriptionsPerMessage.get(eventSuperType));
+            }
+        }
+        // IMPROVEMENT: use tree list that sorts during insertion
+        //Collections.sort(subscriptions, new SubscriptionByPriorityDesc());
+        return subscriptions;
+    }
+
+    private Collection<Class> getSuperclasses(Class from) {
+        Collection<Class> superclasses = new LinkedList<Class>();
+        while (!from.equals(Object.class)) {
+            superclasses.add(from.getSuperclass());
+            from = from.getSuperclass();
+        }
+        return superclasses;
+    }
+
+    // associate a suscription with a message type
+    private void addMessageTypeSubscription(Class messageType, Subscription subscription) {
+        Collection<Subscription> subscriptions = subscriptionsPerMessage.get(messageType);
+        if (subscriptions == null) {
+            subscriptions = new CopyOnWriteArraySet<Subscription>();
+            subscriptionsPerMessage.put(messageType, subscriptions);
+        }
+        subscriptions.add(subscription);
+    }
+
+
+    private boolean isValidMessageHandler(Method handler) {
+        if (handler.getParameterTypes().length != 1) {
+            // a messageHandler only defines one parameter (the message)
+            System.out.println("Found no or more than one parameter in messageHandler [" + handler.getName()
+                    + "]. A messageHandler must define exactly one parameter");
+            return false;
+        }
+        return true;
+    }
+
+    private static Class getMessageType(Method listener) {
+        return listener.getParameterTypes()[0];
+    }
+
+    // get all listeners defined by the given class (includes
+    // listeners defined in super classes)
+    private static List<Method> getListeners(Class<?> target) {
+        return ReflectionUtils.getMethods(AllMessageListeners, target);
+    }
+
+
+    public void handlePublicationError(PublicationError error) {
+        for (IPublicationErrorHandler errorHandler : errorHandlers)
+            errorHandler.handleError(error);
+    }
+
+    @Override
+    protected void finalize() throws Throwable {
+        super.finalize();
+        for (Thread dispatcher : dispatchers) {
+            dispatcher.interrupt();
+        }
+    }
+
+    @Override
+    public Executor getExecutor() {
+        return executor;
+    }
+
+}
```
</details>


### with hunks
#### tokenized log

<details>
<summary>R96</summary>
 
```
====== DIFF: a/src/main/java/org/mbassy/MBassador#private_void_initDispatcherThreads(int).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_void_initDispatcherThreads(int).mjava b/src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava
similarity index 96%
rename from src/main/java/org/mbassy/MBassador#private_void_initDispatcherThreads(int).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava
index 191afbf..6d8a8cc 100644
--- a/src/main/java/org/mbassy/MBassador#private_void_initDispatcherThreads(int).mjava
+++ b/src/main/java/org/mbassy/AbstractMessageBus#private_void_initDispatcherThreads(int).mjava
@@ -45,13 +45,14 @@ true	TRUE
 {	LEFTWHILEBRACKET
 try	TRY
 {	LEFTTRYBRACKET
-publish	INVOKEDMETHODNAME
-(	LEFTMETHODINVOCATIONPAREN
 pendingMessages	VARIABLENAME
 .	DOT
 take	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
+.	DOT
+execute	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 }	RIGHTTRYBRACKET
@@ -61,9 +62,7 @@ InterruptedException	TYPENAME
 e	VARIABLENAME
 )	RIGHTCATCHCLAUSEPAREN
 {	LEFTCATCHCLAUSEBRACKET
-errorHandler	VARIABLENAME
-.	DOT
-handleError	INVOKEDMETHODNAME
+handlePublicationError	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
 new	NEW
 PublicationError	TYPENAME
```
</details>


<details>
<summary>R91</summary>

```
====== DIFF: a/src/main/java/org/mbassy/MBassador#public_void_subscribe(Object).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#public_void_subscribe(Object).mjava b/src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava
similarity index 91%
rename from src/main/java/org/mbassy/MBassador#public_void_subscribe(Object).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava
index 18e28a2..2e10805 100644
--- a/src/main/java/org/mbassy/MBassador#public_void_subscribe(Object).mjava
+++ b/src/main/java/org/mbassy/AbstractMessageBus#public_void_subscribe(Object).mjava
@@ -6,6 +6,8 @@ Object	TYPENAME
 listener	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
+try	TRY
+{	LEFTTRYBRACKET
 Class	TYPENAME
 listeningClass	VARIABLENAME
 =	ASSIGN
@@ -130,23 +132,6 @@ messageHandler	VARIABLENAME
 )	RIGHTIFPAREN
 continue	CONTINUE
 ;	CONTINUESTATEMENTSEMICOLON
-MessageFilter	TYPENAME
-[	LEFTSQUAREBRACKET
-]	RIGHTSQUAREBRACKET
-filter	VARIABLENAME
-=	ASSIGN
-getFilter	INVOKEDMETHODNAME
-(	LEFTMETHODINVOCATIONPAREN
-messageHandler	VARIABLENAME
-.	DOT
-getAnnotation	INVOKEDMETHODNAME
-(	LEFTMETHODINVOCATIONPAREN
-Listener	TYPENAME
-.	DOT
-class	CLASS
-)	RIGHTMETHODINVOCATIONPAREN
-)	RIGHTMETHODINVOCATIONPAREN
-;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 Class	TYPENAME
 eventType	VARIABLENAME
 =	ASSIGN
@@ -158,11 +143,16 @@ messageHandler	VARIABLENAME
 Subscription	TYPENAME
 subscription	VARIABLENAME
 =	ASSIGN
+subscriptionFactory	VARIABLENAME
+.	DOT
 createSubscription	INVOKEDMETHODNAME
 (	LEFTMETHODINVOCATIONPAREN
+metadataReader	VARIABLENAME
+.	DOT
+getHandlerMetadata	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
 messageHandler	VARIABLENAME
-,	METHODINVOCATIONCOMMA
-filter	VARIABLENAME
+)	RIGHTMETHODINVOCATIONPAREN
 )	RIGHTMETHODINVOCATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 subscription	VARIABLENAME
@@ -213,4 +203,19 @@ subscribe	INVOKEDMETHODNAME
 listener	VARIABLENAME
 )	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
+}	RIGHTTRYBRACKET
+catch	CATCH
+(	LEFTCATCHCLAUSEPAREN
+Exception	TYPENAME
+e	VARIABLENAME
+)	RIGHTCATCHCLAUSEPAREN
+{	LEFTCATCHCLAUSEBRACKET
+throw	THROW
+new	NEW
+RuntimeException	TYPENAME
+(	LEFTCLASSINSTANCECREATIONPAREN
+e	VARIABLENAME
+)	RIGHTCLASSINSTANCECREATIONPAREN
+;	THROWSTATEMENTSEMICOLON
+}	RIGHTCATCHCLAUSEBRACKET
 }	RIGHTMETHODBRACKET
```
</details>


| **Refactoring Type**         | **Detailed Changes** |
|-----------------------------|------------------------------------------------------------|
| **Extract Superclass**       | Extracted `AbstractMessageBus.java` as a new superclass to centralize the message bus logic that was previously in `MBassador.java` |
| **Move Method**              | Multiple methods from `MBassador.java`, such as `subscribe()`, `unsubscribe()`, `handlePublicationError()`, and `getSubscriptionsByMessageType()`, were moved to `AbstractMessageBus.java` |
| **Change Method Access Modifier** | `getSubscriptionsByMessageType()` was changed from `private` to `protected`, `handlePublicationError(PublicationError error)` was changed from `private` to `public` |
| **Rename Method** | ❌ Method behavior was changed |




# Move and Rename Method
### Three Types  
| Path Change       | Class Name Change       | Method Name Change | Count |
|-------------------|------------------------|--------------------|-------|
| Same path        | Different class names   | Different methods  | 3     |
| Different paths  | Different class names   | Different methods  | 0     |
| Different paths  | Same class name         | Different methods  | 0     |



| repository_name | commit_id | file_similarity_score | change_type | change_type_info | old_filename | new_filename |
|----------------|-----------|----------------------|----------------------|------------------|--------------|--------------|
| mbassador | f8c5bbe | 93 | Move and Rename Method | 'private_Collection[Subscription]_getSubscriptionsByMessageType' at 'src/main/java/org/mbassy/MBassador' to 'protected_Collection[Subscription]_getSubscriptionsByMessageType' at 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava | src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava |
| mbassador | f8c5bbe | 60 | Move and Rename Method | 'public_void_setErrorHandler' at 'src/main/java/org/mbassy/MBassador' to 'public_void_addErrorHandler' at 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#public_void_setErrorHandler(IPublicationErrorHandler).mjava | src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava |
| mbassador | f8c5bbe | 67 | Move and Rename Method | 'private_void_handlePublicationError' at 'src/main/java/org/mbassy/MBassador' to 'public_void_handlePublicationError' at 'src/main/java/org/mbassy/AbstractMessageBus' | src/main/java/org/mbassy/MBassador#private_void_handlePublicationError(PublicationError).mjava | src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava |

#### tokenized log

<details>
<summary>R93</summary>
 
```
====== DIFF: a/src/main/java/org/mbassy/MBassador#private_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava b/src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
similarity index 93%
rename from src/main/java/org/mbassy/MBassador#private_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
index 59438b4..aa7d902 100644
--- a/src/main/java/org/mbassy/MBassador#private_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
+++ b/src/main/java/org/mbassy/AbstractMessageBus#protected_Collection[Subscription]_getSubscriptionsByMessageType(Class).mjava
@@ -1,4 +1,4 @@
-private	PRIVATE
+protected	PROTECTED
 Collection	TYPENAME
 <	LESS
 Subscription	TYPENAME
@@ -9,18 +9,21 @@ Class	TYPENAME
 messageType	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
-List	TYPENAME
+Set	TYPENAME
 <	LESS
 Subscription	TYPENAME
 >	GREAT
 subscriptions	VARIABLENAME
 =	ASSIGN
 new	NEW
-LinkedList	TYPENAME
+TreeSet	TYPENAME
 <	LESS
 Subscription	TYPENAME
 >	GREAT
 (	LEFTCLASSINSTANCECREATIONPAREN
+Subscription	VARIABLENAME
+.	DOT
+SubscriptionByPriorityDesc	VARIABLENAME
 )	RIGHTCLASSINSTANCECREATIONPAREN
 ;	VARIABLEDECLARATIONSTATEMENTSEMICOLON
 if	IF
```
</details>

<details>
<summary>R60</summary>

```
====== DIFF: a/src/main/java/org/mbassy/MBassador#public_void_setErrorHandler(IPublicationErrorHandler).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#public_void_setErrorHandler(IPublicationErrorHandler).mjava b/src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
similarity index 60%
rename from src/main/java/org/mbassy/MBassador#public_void_setErrorHandler(IPublicationErrorHandler).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
index 3d4158a..a2108fe 100644
--- a/src/main/java/org/mbassy/MBassador#public_void_setErrorHandler(IPublicationErrorHandler).mjava
+++ b/src/main/java/org/mbassy/AbstractMessageBus#public_void_addErrorHandler(IPublicationErrorHandler).mjava
@@ -1,15 +1,16 @@
 public	PUBLIC
 void	VOID
-setErrorHandler	DECLAREDMETHODNAME
+addErrorHandler	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
 IPublicationErrorHandler	TYPENAME
 handler	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
-this	THIS
+errorHandlers	VARIABLENAME
 .	DOT
-errorHandler	VARIABLENAME
-=	ASSIGN
+add	INVOKEDMETHODNAME
+(	LEFTMETHODINVOCATIONPAREN
 handler	VARIABLENAME
+)	RIGHTMETHODINVOCATIONPAREN
 ;	EXPRESSIONSTATEMENTSEMICOLON
 }	RIGHTMETHODBRACKET
```
 
</details> 

<details>
<summary>R67</summary>

```
====== DIFF: a/src/main/java/org/mbassy/MBassador#private_void_handlePublicationError(PublicationError).mjava ======
diff --git a/src/main/java/org/mbassy/MBassador#private_void_handlePublicationError(PublicationError).mjava b/src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava
similarity index 67%
rename from src/main/java/org/mbassy/MBassador#private_void_handlePublicationError(PublicationError).mjava
rename to src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava
index 2b93a68..88a8d13 100644
--- a/src/main/java/org/mbassy/MBassador#private_void_handlePublicationError(PublicationError).mjava
+++ b/src/main/java/org/mbassy/AbstractMessageBus#public_void_handlePublicationError(PublicationError).mjava
@@ -1,4 +1,4 @@
-private	PRIVATE
+public	PUBLIC
 void	VOID
 handlePublicationError	DECLAREDMETHODNAME
 (	LEFTMETHODPAREN
@@ -6,6 +6,13 @@ PublicationError	TYPENAME
 error	VARIABLENAME
 )	RIGHTMETHODPAREN
 {	LEFTMETHODBRACKET
+for	FOR
+(	LEFTENHANCEDFORPAREN
+IPublicationErrorHandler	TYPENAME
+errorHandler	VARIABLENAME
+:	COLON
+errorHandlers	VARIABLENAME
+)	RIGHTENHANCEDFORPAREN
 errorHandler	VARIABLENAME
 .	DOT
 handleError	INVOKEDMETHODNAME
```

</details> 

</details>
