from django import template

register = template.Library()


@register.inclusion_tag("components/table_of_contents.html")
def table_of_contents(entries_list):
    return {"entries_list": entries_list}


@register.inclusion_tag("components/template_child_entry.html")
def template_child_entry(template_child):
    return {"template_child": template_child}


@register.inclusion_tag("components/template_page.html")
def template_page(template, template_children, template_children_type):
    return {
        "template": template,
        "template_children": template_children,
        "template_children_type": template_children_type,
    }
