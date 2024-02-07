function Link(el)
  el.target = string.gsub(el.target, "%.md", ".html")
  el.target = string.gsub(el.target, "%.rawmd", ".md")
  return el
end

function Image(el)
  el.src = string.gsub(el.src, "../assets", "assets")
  return el
end

function CodeBlock(el)
  el.text = string.gsub(el.text, "(.+)", "    %0")
  return el
end
