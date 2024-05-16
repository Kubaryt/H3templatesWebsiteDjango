from django import template

register = template.Library()


@register.inclusion_tag("components/table_of_contents.html")
def table_of_contents(entries_list):
    return {"entries_list": entries_list}
