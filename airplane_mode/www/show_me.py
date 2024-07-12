import frappe


def get_context(context):
    # Get the color query parameter
    color = frappe.form_dict.color
    # Pass the color to the template
    context.color = color
    return context
