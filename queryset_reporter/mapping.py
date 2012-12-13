# -*- encoding: utf-8 -*-

'''
mapping of lookups and fields.
'''

from django.utils.translation import ugettext_lazy as _

LOOKUPS = (
    ('exact', _(u'Termo exato')),
    ('iexact', _(u'Termo exato (case-insensitivo)')),
    ('contains', _(u'Contém o termo')),
    ('icontains', _(u'Contém o termo (case-insensitivo)')),
    ('in', _(u'Termo está na lista')),
    ('gt', _(u'Maior que')),
    ('gte', _(u'Maior ou igual que')),
    ('lt', _(u'Menor que')),
    ('lte', _(u'Menor ou igual que')),
    ('startswith', _(u'Começa com')),
    ('istartswith', _(u'Começa com (case-insensitivo)')),
    ('endswith', _(u'Termina com')),
    ('iendswith', _(u'Termina com (case-insensitivo)')),
    ('range', _(u'Faixa/período')),
    ('year', _(u'Ano específico')),
    ('month', _(u'Mês específico')),
    ('day', _(u'Dia específico.')),
    ('isnull', _(u'É nulo?')),
    ('search', _(u'Busca textual')),  # mysql
    ('regex', _(u'Expressão regular')),
    ('iregex', _(u'Expressão regular (case-insensitivo)')),
)

_NUMERICAL_LOOKUP = {
    'exact': (1, 'numerical-field'),
    'iexact': (1, 'numerical-field'),
    'contains': None,
    'icontains': None,
    'in': (1, 'numerical-list'),
    'gt': (1, 'numerical-field'),
    'gte': (1, 'numerical-field'),
    'lt': (1, 'numerical-field'),
    'lte': (1, 'numerical-field'),
    'startswith': None,
    'istartswith': None,
    'endswith': None,
    'iendswith': None,
    'range': (2, 'numerical-field'),
    'year': None,
    'month': None,
    'day': None,
    'isnull': (1, 'boolean-field'),
    'search': None,
    'regex': None,
    'iregex': None,
}

_CHAR_LOOKUP = {
    'exact': (1, 'char-field'),
    'iexact': (1, 'char-field'),
    'contains': (1, 'char-field'),
    'icontains': (1, 'char-field'),
    'in': (1, 'char-list'),
    'gt': None,
    'gte': None,
    'lt': None,
    'lte': None,
    'startswith': (1, 'char-field'),
    'istartswith': (1, 'char-field'),
    'endswith': (1, 'char-field'),
    'iendswith': (1, 'char-field'),
    'range': (2, 'numerical-field'),
    'year': None,
    'month': None,
    'day': None,
    'isnull': (1, 'boolean-field'),
    'search': (1, 'char-field'),
    'regex': (1, 'char-field'),
    'iregex': (1, 'char-field'),
}

_DATETIME_LOOKUP = {
    'exact': (1, 'datetime-field'),
    'iexact': (1, 'datetime-field'),
    'contains': None,
    'icontains': None,
    'in': None,
    'gt': (1, 'datetime-field'),
    'gte': (1, 'datetime-field'),
    'lt': (1, 'datetime-field'),
    'lte': (1, 'datetime-field'),
    'startswith': None,
    'istartswith': None,
    'endswith': None,
    'iendswith': None,
    'range': (2, 'datetime-field'),
    'year': (1, 'numerical-field'),
    'month': (1, 'numerical-field'),
    'day': (1, 'numerical-field'),
    'isnull': (1, 'boolean-field'),
    'search': None,
    'regex': None,
    'iregex': None,
}

_BOOLEAN_LOOKUP = {
    'exact': (1, 'boolean-field'),
    'iexact': None,
    'contains': None,
    'icontains': None,
    'in': None,
    'gt': None,
    'gte': None,
    'lt': None,
    'lte': None,
    'startswith': None,
    'istartswith': None,
    'endswith': None,
    'iendswith': None,
    'range': None,
    'year': None,
    'month': None,
    'day': None,
    'isnull': (1, 'boolean-field'),
    'search': None,
    'regex': None,
    'iregex': None,
}

_RELATED_LOOKUP = {
    'exact': (1, 'numerical-field'),
    'iexact': None,
    'contains': None,
    'icontains': None,
    'in': (1, 'numerical-list'),
    'gt': None,
    'gte': None,
    'lt': None,
    'lte': None,
    'startswith': None,
    'istartswith': None,
    'endswith': None,
    'iendswith': None,
    'range': None,
    'year': None,
    'month': None,
    'day': None,
    'isnull': (1, 'boolean-field'),
    'search': None,
    'regex': None,
    'iregex': None,
}

LOOKUP_MAPPING = {
    # numericals
    'BigIntegerField': _NUMERICAL_LOOKUP,
    'IntegerField': _NUMERICAL_LOOKUP,
    'DecimalField': _NUMERICAL_LOOKUP,
    'FloatField': _NUMERICAL_LOOKUP,
    'PositiveIntegerField': _NUMERICAL_LOOKUP,
    'PositiveSmallIntegerField': _NUMERICAL_LOOKUP,
    'SmallIntegerField': _NUMERICAL_LOOKUP,
    'AutoField': _NUMERICAL_LOOKUP,
    # relateds
    'RelatedObject': _RELATED_LOOKUP,
    'ManyToManyField': _RELATED_LOOKUP,
    'ForeignKey': _RELATED_LOOKUP,
    'OneToOneField': _RELATED_LOOKUP,
    # chars
    'SlugField': _CHAR_LOOKUP,
    'CharField': _CHAR_LOOKUP,
    'TextField': _CHAR_LOOKUP,
    'EmailField': _CHAR_LOOKUP,
    'FileField': _CHAR_LOOKUP,
    'FilePathField': _CHAR_LOOKUP,
    'ImageField': _CHAR_LOOKUP,
    'IPAddressField': _CHAR_LOOKUP,
    'URLField': _CHAR_LOOKUP,
    'XMLField': _CHAR_LOOKUP,
    # datetime`s
    'DateTimeField': _DATETIME_LOOKUP,
    'DateField': _DATETIME_LOOKUP,
    'TimeField': _DATETIME_LOOKUP,
    # booleans
    'BooleanField': _BOOLEAN_LOOKUP,
}
