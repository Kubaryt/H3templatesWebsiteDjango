from django import template

register = template.Library()


@register.inclusion_tag("components/table_of_contents.html")
def table_of_contents(entries_list):
    return {"entries_list": entries_list}


@register.inclusion_tag("components/template_entry.html")
def template_entry(template):
    return {"template": template}


@register.inclusion_tag("components/../templates/core/template_page.html")
def template_page(template, template_children, template_children_type):
    return {
        "template": template,
        "template_children": template_children,
        "template_children_type": template_children_type,
    }
