#!/usr/bin/ruby
require 'redcarpet'
print "Content-type: text/html\n\n"
markdown = Redcarpet::Markdown.new(
    Redcarpet::Render::HTML,
    :autolink => true,
    :fenced_code_blocks => true,
)
puts markdown.render(File.read(ENV['PATH_TRANSLATED']))
