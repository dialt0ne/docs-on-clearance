#!/usr/bin/ruby
#
# Markdown.cgi
#
#   Copyright 2014 Corsis
#   http://www.corsis.com/
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

require 'digest/md5'
require 'redcarpet'
require 'memcache'

CACHETIME = 300
CACHE = MemCache.new('127.0.0.1')

private
def data_cache(key)
  unless output = CACHE.get(key)
    output = yield
    CACHE.set(key, output, CACHETIME)
  end
  return output
end

print "Content-type: text/html\n\n"
markdown = Redcarpet::Markdown.new(
    Redcarpet::Render::XHTML,
    :autolink => true,
    :strikethrough => true,
    :superscript => true,
    :underline => true,
    :highlight => true,
    :fenced_code_blocks => true,
)
uri = ENV['PATH_TRANSLATED']
key = Digest::MD5.hexdigest(uri)
puts data_cache(key) {
    "<!DOCTYPE html>\n" + 
    "<html>\n" + 
    "<head>\n" + 
    "<link rel='stylesheet' href='//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css'>\n" + 
    "<style type='text/css'>\n" + 
    ".container { margin: 20 0 20 0; }\n" + 
    "</style>\n" + 
    "</head>\n" + 
    "<body>\n" +
    "<div class='container'>\n" +
    "<script src='//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js'></script>\n" +
    "<script src='//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js'></script>\n" +
    markdown.render(File.read(uri)) +
    "</div>\n" +
    "</body>\n" +
    "</html>"
}
