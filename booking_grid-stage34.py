# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: BookingGrid
def apply_template(self, template_name, **overrides):
    templates = getattr(self, '_templates', {})
    if template_name not in templates:
        raise ValueError(f"Unknown template: {template_name!r}")
    tmpl = templates[template_name].copy()
    tmpl.update(overrides)
    return tmpl

def register_template(self, name, fields, default_values=None):
    if default_values is None:
        default_values = {}
    self._templates.setdefault(name, list(fields))
    return self
