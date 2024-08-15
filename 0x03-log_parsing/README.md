
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate"

<meta name="csrf-token" content="GG_RyBqIKJYIxVfc-8Iwb8lx8jjJ_CUuMhAZA_Kq86g_lTIZDE69IlXnn8wifqbt4DXMCBSXGZ7wbnlgS6CgCw" />
  </head>

  <body class="signed_in env_production notranslate"
    <p>For the &ldquo;0x03. Log Parsing&rdquo; project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. 
This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. 
Here&rsquo;s a list of concepts and resources that you might find useful:</p>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>File I/O in Python</strong>:</p>

<ul>
<li>Understand how to read from <code>sys.stdin</code> line by line.</li>
<li><a href="/rltoken/f7U2MDsBT_rd9AfUUaqVnQ" title="Python Input and Output" target="_blank">Python Input and Output</a></li>
</ul></li>
<li><p><strong>Signal Handling in Python</strong>:</p>

<ul>
<li>Handling keyboard interruption (CTRL + C) using signal handling in Python.</li>
<li><a href="/rltoken/1nDqPJe80rSD-NMulzjJBw" title="Python Signal Handling" target="_blank">Python Signal Handling</a></li>
</ul></li>
<li><p><strong>Data Processing</strong>:</p>

<ul>
<li>Parsing strings to extract specific data points.</li>
<li>Aggregating data to compute summaries.</li>
</ul></li>
<li><p><strong>Regular Expressions</strong>:</p>

<ul>
<li>Using regular expressions to validate the format of each line.</li>
<li><a href="/rltoken/ZsD-YLisfaHFeMT_sZxX1Q" title="Python Regular Expressions" target="_blank">Python Regular Expressions</a></li>
</ul></li>
<li><p><strong>Dictionaries in Python</strong>:</p>

<ul>
<li>Using dictionaries to count occurrences of status codes and accumulate file sizes.</li>
<li><a href="/rltoken/JM-RpavKkb8yanxWEnNYJw" title="Python Dictionaries" target="_blank">Python Dictionaries</a></li>
</ul></li>
<li><p><strong>Exception Handling</strong>:</p>

<ul>
<li>Handling possible exceptions that may arise during file reading and data processing.</li>
<li><a href="/rltoken/OA2PlryrYA2gyCCKIsdgUw" title="Python Exceptions" target="_blank">Python Exceptions</a></li>
</ul></li>
</ol>

<p>By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.</p>

<h2>Additional Resources</h2>

<ul>
<li><a href="/rltoken/VlOaXKkbecRYdnTLaLU1lg" title="Mock Technical Interview" target="_blank">Mock Technical Interview</a></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.x)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

## Task Body
Write a script that reads <code>stdin</code> line by line and computes metrics:

<ul>
<li>Input format: <code>;IP Address; - [date];GET /projects/260 HTTP/1.1;status code file size;</code> (if the format is not this one, the line must be skipped)</li>
<li>After every 10 lines and/or a keyboard interruption (<code>CTRL + C</code>), print these statistics from the beginning:

<ul>
<li>Total file size: <code>File size: &lt;total size&gt;</code></li>
<li>where <code>&lt;total size&gt;</code> is the sum of all previous <code>&lt;file size&gt;</code> (see input format above)</li>
<li>Number of lines by status code: 

<ul>
<li>possible status code: <code>200</code>, <code>301</code>, <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code>, <code>405</code> and <code>500</code></li>
<li>if a status code doesn&rsquo;t appear or is not an integer, don&rsquo;t print anything for this status code</li>
<li>format: <code>&lt;status code&gt;: &lt;number&gt;</code></li>
<li>status codes should be printed in ascending order</li>
</ul></li>
</ul></li>
</ul>

<p><strong>Warning:</strong> In this sample, you will have random value - it&rsquo;s normal to not have the same output as this one.</p>

<pre><code>alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write(&quot;{:d}.{:d}.{:d}.{:d} - [{}] \&quot;GET /projects/260 HTTP/1.1\&quot; {} {}\n&quot;.format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File &quot;./0-stats.py&quot;, line 15, in &lt;module&gt;
Traceback (most recent call last):
  File &quot;./0-generator.py&quot;, line 8, in &lt;module&gt;
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
</code></pre>
  </body>
</html>
