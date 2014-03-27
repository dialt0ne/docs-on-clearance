#!/usr/bin/ruby
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
