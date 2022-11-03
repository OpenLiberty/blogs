# Instant-On-Test-Intel-Mac

## Test using podman without `rootful` setting 

* podman machine init
* podman machine start

guide-getting-started successfully started normally in 4.861 seconds.
```
htakamiy@us.ibm.com:~/InstantOn/guide-getting-started/finish$ podman run -it --name getting-started --rm -p 9080:9080 getting-started

Launching defaultServer (Open Liberty 22.0.0.12-beta/wlp-1.0.70.cl221120221010-1540) on Eclipse OpenJ9 VM, version 17.0.5-ea+2 (en_US)
CWWKE0953W: This version of Open Liberty is an unsupported early release version.
[AUDIT   ] CWWKE0001I: The server defaultServer has been launched.
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/checkpoint.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/keystore.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/open-default-port.xml
[AUDIT   ] CWWKZ0058I: Monitoring dropins for applications.
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://6e7b1da9020b:9080/metrics/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://6e7b1da9020b:9080/health/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://6e7b1da9020b:9080/ibm/api/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://6e7b1da9020b:9080/dev/
[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 1.755 seconds.
[AUDIT   ] CWWKF0012I: The server installed the following features: [cdi-3.0, checkpoint-1.0, concurrent-2.0, distributedMap-1.0, jndi-1.0, json-1.0, jsonb-2.0, jsonp-2.0, monitor-1.0, mpConfig-3.0, mpHealth-4.0, mpMetrics-4.0, restfulWS-3.0, restfulWSClient-3.0, servlet-5.0, ssl-1.0, transportSecurity-1.0].
[AUDIT   ] CWWKF0011I: The defaultServer server is ready to run a smarter planet. The defaultServer server started in 4.861 seconds.
```
confirmed the function with curl
```
htakamiy@us.ibm.com:~/libertyGit/open-liberty/dev$ curl http://localhost:9080/dev/system/properties
{"awt.toolkit":"sun.awt.X11.XToolkit",..}
```

Starting with `--env WLP_CHECKPOINT=applications` showed the error below although the server started successfully in 5.581 seconds.   
```
CWWKE0084I: The server defaultServer is stopping because thread  Checkpoint failed, exiting... (00000033) called the method java.lang.System.exit:
```
Command output below.

```
htakamiy@us.ibm.com:~/InstantOn/guide-getting-started/finish$ podman run --name getting-started-checkpoint-container --privileged --env WLP_CHECKPOINT=applications getting-started
Performing checkpoint --at=applications

Launching defaultServer (Open Liberty 22.0.0.12-beta/wlp-1.0.70.cl221120221010-1540) on Eclipse OpenJ9 VM, version 17.0.5-ea+2 (en_US)
CWWKE0953W: This version of Open Liberty is an unsupported early release version.
[AUDIT   ] CWWKE0001I: The server defaultServer has been launched.
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/checkpoint.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/keystore.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/open-default-port.xml
[AUDIT   ] CWWKZ0058I: Monitoring dropins for applications.
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://cb6f543f9d1d:9080/ibm/api/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://cb6f543f9d1d:9080/metrics/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://cb6f543f9d1d:9080/health/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://cb6f543f9d1d:9080/dev/
[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 1.240 seconds.
[AUDIT   ] CWWKC0451I: A server checkpoint was requested. When the checkpoint completes, the server stops.
[ERROR   ] CWWKC0453E: The server checkpoint request failed with the following message: Could not dump the JVM processs, err=-52
[AUDIT   ] CWWKF0012I: The server installed the following features: [cdi-3.0, checkpoint-1.0, concurrent-2.0, distributedMap-1.0, jndi-1.0, json-1.0, jsonb-2.0, jsonp-2.0, monitor-1.0, mpConfig-3.0, mpHealth-4.0, mpMetrics-4.0, restfulWS-3.0, restfulWSClient-3.0, servlet-5.0, ssl-1.0, transportSecurity-1.0].
[AUDIT   ] CWWKF0011I: The defaultServer server is ready to run a smarter planet. The defaultServer server started in 5.581 seconds.
[AUDIT   ] CWWKE0084I: The server defaultServer is stopping because thread Checkpoint failed, exiting... (00000033) called the method java.lang.System.exit:
	at java.base/java.lang.System.exit(System.java:488)
	at io.openliberty.checkpoint.internal.CheckpointImpl.lambda$checkpointOrExitOnFailure$1(CheckpointImpl.java:355)
	at java.base/java.lang.Thread.run(Thread.java:857)

[AUDIT   ] CWWKE1100I: Waiting for up to 30 seconds for the server to quiesce.
[AUDIT   ] CWWKT0017I: Web application removed (default_host): http://cb6f543f9d1d:9080/dev/
[AUDIT   ] CWWKT0017I: Web application removed (default_host): http://cb6f543f9d1d:9080/metrics/
[AUDIT   ] CWWKT0017I: Web application removed (default_host): http://cb6f543f9d1d:9080/health/
[AUDIT   ] CWWKT0017I: Web application removed (default_host): http://cb6f543f9d1d:9080/ibm/api/
[AUDIT   ] CWWKZ0009I: The application guide-getting-started has stopped successfully.
```

## Test using podman with `rootful` setting

After the above test, I created podman with rootful setting. Everything seem to go fine but I started to get the following error. 
```
Error: failed to connect: dial tcp [::1]:54160: connect: connection refused
```
The error went away after I removed podman machines and recreate podman machine. 
* podman machine rm xxx 
* podman machine init rootful
* podman machine set --rootful rootful
* podman machine start rootful 
```
htakamiy@us.ibm.com:~$ podman machine init rootful
Extracting compressed file
Image resized.
Machine init complete
To start your machine run:

	podman machine start rootful

htakamiy@us.ibm.com:~$ podman machine set --rootful rootful
htakamiy@us.ibm.com:~$ podman machine start rootful
Error: cannot start VM rootful. VM podman-machine-default is currently running or starting: only one VM can be active at a time
htakamiy@us.ibm.com:~$ podman machine stop
Waiting for VM to exit...
Machine "podman-machine-default" stopped successfully
htakamiy@us.ibm.com:~$ podman machine set --rootful rootful
htakamiy@us.ibm.com:~$ podman machine start rootful
Starting machine "rootful"
Waiting for VM ...
Mounting volume... /Users/htakamiy@us.ibm.com:/Users/htakamiy@us.ibm.com
API forwarding listening on: /Users/htakamiy@us.ibm.com/.local/share/containers/podman/machine/rootful/podman.sock

The system helper service is not installed; the default Docker API socket
address can't be used by podman. If you would like to install it run the
following commands:

	sudo /usr/local/Cellar/podman/4.3.0/bin/podman-mac-helper install
	podman machine stop rootful; podman machine start rootful

You can still connect Docker API clients by setting DOCKER_HOST using the
following command in your terminal session:

	export DOCKER_HOST='unix:///Users/htakamiy@us.ibm.com/.local/share/containers/podman/machine/rootful/podman.sock'

Machine "rootful" started successfully
```
The image is gone, so I started from the following step.  
```
podman build -t getting-started .
```
then started the container and confirmed the application startup using curl before using the `WLP_CHECKPOINT=applications` again.  This time, the checkpoint image was created and committed successfully. 

``` 
podman run --name getting-started-checkpoint-container --privileged --env WLP_CHECKPOINT=applications getting-started
Performing checkpoint --at=applications

Launching defaultServer (Open Liberty 22.0.0.12-beta/wlp-1.0.70.cl221120221010-1540) on Eclipse OpenJ9 VM, version 17.0.5-ea+2 (en_US)
CWWKE0953W: This version of Open Liberty is an unsupported early release version.
[AUDIT   ] CWWKE0001I: The server defaultServer has been launched.
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/checkpoint.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/keystore.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/open-default-port.xml
[AUDIT   ] CWWKZ0058I: Monitoring dropins for applications.
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://1587afe016c2:9080/ibm/api/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://1587afe016c2:9080/health/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://1587afe016c2:9080/metrics/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://1587afe016c2:9080/dev/
[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 1.534 seconds.
[AUDIT   ] CWWKC0451I: A server checkpoint was requested. When the checkpoint completes, the server stops.
/opt/ol/wlp/bin/server: line 951:   130 Killed                  "${JAVA_CMD}" "$@" >> "${CHECKPOINT_CONSOLE_LOG}" 2>&1 < /dev/null
```
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman commit getting-started-checkpoint-container getting-started-instanton
984c259b5081bd0a56d8d5f848e59ee2c6731f73814b3020e785a072e971a586
```
I started the InstantOn without `--privilege` . I was curious to see if the `rootful podman` already has the privilege. But it took 6.676 seconds.
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman run --rm -p 9080:9080 getting-started-instanton

/opt/ol/wlp/bin/server: line 1413: /usr/sbin/criu: Operation not permitted
CWWKE0957I: Restoring the checkpoint server process failed. Check the /logs/checkpoint/restore.log log to determine why the checkpoint process was not restored. Launching the server without using the checkpoint image.
Launching defaultServer (Open Liberty 22.0.0.12-beta/wlp-1.0.70.cl221120221010-1540) on Eclipse OpenJ9 VM, version 17.0.5-ea+2 (en_US)
CWWKE0953W: This version of Open Liberty is an unsupported early release version.
[AUDIT   ] CWWKE0001I: The server defaultServer has been launched.
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/checkpoint.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/keystore.xml
[AUDIT   ] CWWKG0093A: Processing configuration drop-ins resource: /opt/ol/wlp/usr/servers/defaultServer/configDropins/defaults/open-default-port.xml
[AUDIT   ] CWWKZ0058I: Monitoring dropins for applications.
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://54a1dc276fad:9080/ibm/api/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://54a1dc276fad:9080/metrics/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://54a1dc276fad:9080/health/
[AUDIT   ] CWWKT0016I: Web application available (default_host): http://54a1dc276fad:9080/dev/
[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 1.438 seconds.
[AUDIT   ] CWWKF0012I: The server installed the following features: [cdi-3.0, checkpoint-1.0, concurrent-2.0, distributedMap-1.0, jndi-1.0, json-1.0, jsonb-2.0, jsonp-2.0, monitor-1.0, mpConfig-3.0, mpHealth-4.0, mpMetrics-4.0, restfulWS-3.0, restfulWSClient-3.0, servlet-5.0, ssl-1.0, transportSecurity-1.0].
[AUDIT   ] CWWKF0011I: The defaultServer server is ready to run a smarter planet. The defaultServer server started in 6.676 seconds.
```
I added `--privilege` and saw the InstantOn working for the first time. (The server started in 0.243 seconds.)

```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman run --rm --privileged -p 9080:9080 getting-started-instanton

[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 0.098 seconds.
[AUDIT   ] CWWKC0452I: The Liberty server process resumed operation from a checkpoint in 0.209 seconds.
[AUDIT   ] CWWKF0012I: The server installed the following features: [cdi-3.0, checkpoint-1.0, concurrent-2.0, distributedMap-1.0, jndi-1.0, json-1.0, jsonb-2.0, jsonp-2.0, monitor-1.0, mpConfig-3.0, mpHealth-4.0, mpMetrics-4.0, restfulWS-3.0, restfulWSClient-3.0, servlet-5.0, ssl-1.0, transportSecurity-1.0].
[AUDIT   ] CWWKF0011I: The defaultServer server is ready to run a smarter planet. The defaultServer server started in 0.243 seconds.
``` 
One of the restore commands worked. I was not able to get the other one using `criuRequiredSyscalls.json` failed.

Successful restore.
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman run \
  --rm \
  --cap-add=CHECKPOINT_RESTORE \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  --security-opt systempaths=unconfined \
  --security-opt apparmor=unconfined \
  -p 9080:9080 \
  getting-started-instanton

[AUDIT   ] CWWKZ0001I: Application guide-getting-started started in 0.101 seconds.
[AUDIT   ] CWWKC0452I: The Liberty server process resumed operation from a checkpoint in 0.229 seconds.
[AUDIT   ] CWWKF0012I: The server installed the following features: [cdi-3.0, checkpoint-1.0, concurrent-2.0, distributedMap-1.0, jndi-1.0, json-1.0, jsonb-2.0, jsonp-2.0, monitor-1.0, mpConfig-3.0, mpHealth-4.0, mpMetrics-4.0, restfulWS-3.0, restfulWSClient-3.0, servlet-5.0, ssl-1.0, transportSecurity-1.0].
[AUDIT   ] CWWKF0011I: The defaultServer server is ready to run a smarter planet. The defaultServer server started in 0.283 seconds
```
I created `criuRequiredSysCalls.json` in the directory... 
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman run \
  --rm \
  --cap-add=CHECKPOINT_RESTORE \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=~/InstantOn/guide-getting-started/finish/criuRequiredSysCalls.json \
  -v /proc/sys/kernel/ns_last_pid:/proc/sys/kernel/ns_last_pid \
  -p 9080:9080 \
  getting-started-instanton
Error: opening seccomp profile failed: open ~/InstantOn/guide-getting-started/finish/criuRequiredSysCalls.json: no such file or directory
```
I don't seem to have `/usr/share/containers/seccomp.json`. 
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ ls /usr/share/c
calendar/                  com.apple.languageassetd/  cracklib/                  cups/
```
My podman's `ociRuntime` was `crun`.
```
htakamiy@us.ibm.com|prod=:~/InstantOn/guide-getting-started/finish$ podman info | grep -A 10 ociRuntime
  ociRuntime:
    name: crun
    package: crun-1.6-2.fc36.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.6
      commit: 18cf2efbb8feb2b2f20e316520e0fd0b6c41ef4d
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +YAJL
  os: linux
  remoteSocket:
```





