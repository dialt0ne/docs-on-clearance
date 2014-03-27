Docs on Clearance
=================

e.g. How to enable Markdown on your apache web server

### Features

* Installs easily on an [Apache](http://httpd.apache.org/) webserver
* Renders markdown using the [redcarpet](https://github.com/vmg/redcarpet) gem
* Caches generated page in [memcached](http://memcached.org/) for 5 minutes
* Uses [Bootstrap](http://getbootstrap.com/) from a CDN for nice look and responsive design

### Installation

This installation is for setup on Ubuntu system.

* install prerequisites:

```
sudo apt-get install ruby-redcarpet ruby-memcache-client memcached
sudo service memcached start
```

* install `Markdown.cgi` in your cgi-bin directory

```
sudo cp Markdown.cgi /usr/lib/cgi-bin
sudo chmod +x /usr/lib/cgi-bin/Markdown.cgi
```

* include the apache config snippet to create a CGI handler that will have all .md files handled by `Markdown.cgi`

```
sudo cp enable-markdown.conf /etc/apache2/conf-available
sudo a2enconf enable-markdown
sudo service apache2 reload
```

### ToDo

* work out installation on CentOS/RHEL/Amazon Linux
* move off depricated memcache-client gem

### License

Copyright 2014 Corsis
http://www.corsis.com/

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

