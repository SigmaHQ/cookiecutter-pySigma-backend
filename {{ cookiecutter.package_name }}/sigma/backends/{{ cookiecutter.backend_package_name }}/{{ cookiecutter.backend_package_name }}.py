from sigma.conversion.state import ConversionState
from sigma.rule import SigmaRule
from sigma.conversion.base import TextQueryBackend
from sigma.types import SigmaCompareExpression
from sigma.pipelines.{{ cookiecutter.backend_package_name }} import # TODO: add pipeline imports or delete this line
import sigma
from typing import ClassVar, Dict, List, Optional, Tuple

class {{ cookiecutter.backend_class_name }}(TextQueryBackend):
    """{{ cookiecutter.target_name }} backend."""
    # TODO: change the token definitions according to the syntax.
    # See the pySigma documentation for further infromation:
    # https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html
    group_expression : ClassVar[str] = "({expr})"

    or_token : ClassVar[str] = "OR"
    and_token : ClassVar[str] = " "
    not_token : ClassVar[str] = "NOT"
    eq_token : ClassVar[str] = "="

    str_quote : ClassVar[str] = '"'
    escape_char : ClassVar[str] = "\\"
    wildcard_multi : ClassVar[str] = "*"
    wildcard_single : ClassVar[str] = "*"
    add_escaped : ClassVar[str] = "\\"

    re_expression : ClassVar[str] = "{regex}"
    re_escape_char : ClassVar[str] = "\\"
    re_escape : ClassVar[Tuple[str]] = ('"',)

    cidr_expression : ClassVar[str] = "{value}"

    compare_op_expression : ClassVar[str] = "{field}{operator}{value}"
    compare_operators : ClassVar[Dict[SigmaCompareExpression.CompareOperators, str]] = {
        SigmaCompareExpression.CompareOperators.LT  : "<",
        SigmaCompareExpression.CompareOperators.LTE : "<=",
        SigmaCompareExpression.CompareOperators.GT  : ">",
        SigmaCompareExpression.CompareOperators.GTE : ">=",
    }

    field_null_expression : ClassVar[str] = "{field}!=*"

    convert_or_as_in : ClassVar[bool] = True
    convert_and_as_in : ClassVar[bool] = False
    in_expressions_allow_wildcards : ClassVar[bool] = True
    field_in_list_expression : ClassVar[str] = "{field} {op} ({list})"
    or_in_operator : ClassVar[Optional[str]] = "IN"
    list_separator : ClassVar[str] = ", "

    unbound_value_str_expression : ClassVar[str] = '"{value}"'
    unbound_value_num_expression : ClassVar[str] = '{value}'
    unbound_value_re_expression : ClassVar[str] = '{value}'

    deferred_start : ClassVar[str] = "\n| "
    deferred_separator : ClassVar[str] = "\n| "
    deferred_only_query : ClassVar[str] = "*"

    # TODO: implement custom classes for query elements not covered by the default backend base.
    # Documentation: https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html

    {% if cookiecutter.additional_output_formats %}
    {% for format in cookiecutter.output_formats.split(",") %}
    def finalize_query_{{ format }}(self, rule: SigmaRule, query: str, index: int, state: ConversionState) -> str:
        # TODO: implement the per-query output for the output format {{ format }} here. Usually, the generated query is
        # embedded into a template, e.g. a JSON format with additional information from the Sigma rule.
        return query

    def finalize_output_{{ format }}(self, queries: List[str]) -> str:
        # TODO: implement the output finalization for all generated queries for the format {{ format }} here. Usually,
        # the single generated queries are embedded into a structure, e.g. some JSON or XML that can be imported into
        # the SIEM.
        return "\n".join(queries)
    {% endfor %}
    {% endif %}