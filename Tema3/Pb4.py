def build_xml_element(tag, content, **args):
    attr = ""
    for k, val in args.items():
        attr += f' {k}="{val}"'

    return f'<{tag}{attr}>{content}</{tag}>'

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)