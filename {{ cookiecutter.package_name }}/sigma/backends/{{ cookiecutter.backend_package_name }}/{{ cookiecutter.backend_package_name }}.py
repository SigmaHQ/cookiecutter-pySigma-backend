from sigma.conditions import ConditionAND, ConditionItem, ConditionNOT, ConditionOR
from sigma.conversion.base import TextQueryBackend
from sigma.conversion.deferred import DeferredQueryExpression
from sigma.conversion.state import ConversionState
from sigma.correlations import SigmaCorrelationConditionOperator, SigmaCorrelationRule
from sigma.rule import SigmaRule
from sigma.types import (
    SigmaCompareExpression,
    SigmaRegularExpressionFlag,
    SigmaTimestampPart,
)
# from sigma.pipelines.{{ cookiecutter.backend_package_name }} import ...  # TODO: add pipeline imports or delete this line
import re
from typing import Any, ClassVar, Dict, List, Optional, Pattern, Tuple


class {{ cookiecutter.backend_class_name }}(TextQueryBackend):
    """{{ cookiecutter.target_name }} backend."""

    # TODO: change the token definitions according to the syntax. Delete these not supported by your backend.
    # See the pySigma documentation for further information:
    # https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html

    # Operator precedence: tuple of Condition{AND,OR,NOT} in order of precedence.
    # The backend generates grouping if required.
    name: ClassVar[str] = "{{ cookiecutter.target_name }} backend"
    formats: Dict[str, str] = {
        "default": "Plain {{ cookiecutter.target_name }} queries",
        {% if cookiecutter.additional_output_formats %}
        {% for format in cookiecutter.output_formats.split(",") %}
        "{{ format }}": "'{{ format }}' output format",
        {% endfor %}
        {% endif %}
    }
    requires_pipeline: bool = False  # TODO: Set to True if a processing pipeline is required.

    precedence: ClassVar[Tuple[ConditionItem, ConditionItem, ConditionItem]] = (
        ConditionNOT,
        ConditionAND,
        ConditionOR,
    )
    group_expression: ClassVar[str] = "({expr})"  # Expression for precedence override grouping.
    parenthesize: bool = False  # Set True if the target has no strict precedence handling.

    # Query structure
    query_expression: ClassVar[str] = "{query}"
    state_defaults: ClassVar[Dict[str, str]] = {}

    # Generated query tokens
    token_separator: str = " "  # Separator inserted between all boolean operators
    or_token: ClassVar[str] = "OR"
    and_token: ClassVar[str] = " "
    not_token: ClassVar[str] = "NOT"
    eq_token: ClassVar[str] = "="  # Token inserted between field and value (without separator)
    not_eq_token: ClassVar[Optional[str]] = None
    eq_expression: ClassVar[str] = "{field}{backend.eq_token}{value}"
    not_eq_expression: ClassVar[str] = "{field}{backend.not_eq_token}{value}"

    # String output
    ## Fields
    ### Quoting
    field_quote: ClassVar[str] = "'"  # Field quoting character.
    field_quote_pattern: ClassVar[Pattern] = re.compile(r"^\w+$")
    field_quote_pattern_negation: ClassVar[bool] = True

    ### Escaping
    field_escape: ClassVar[str] = "\\"
    field_escape_quote: ClassVar[bool] = True
    field_escape_pattern: ClassVar[Pattern] = re.compile(r"\s")
    add_escaped_re: ClassVar[str] = ""

    ## Values
    str_quote: ClassVar[str] = '"'
    str_quote_pattern: ClassVar[Optional[Pattern]] = None
    str_quote_pattern_negation: ClassVar[bool] = True
    escape_char: ClassVar[str] = "\\"
    wildcard_multi: ClassVar[str] = "*"
    wildcard_single: ClassVar[str] = "*"
    add_escaped: ClassVar[str] = "\\"
    filter_chars: ClassVar[str] = ""
    bool_values: ClassVar[Dict[bool, str]] = {
        True: "true",
        False: "false",
    }

    # String matching operators. If none is appropriate, eq_token/not_token is used.
    startswith_expression: ClassVar[str] = "{field} startswith {value}"
    not_startswith_expression: ClassVar[Optional[str]] = None
    startswith_expression_allow_special: ClassVar[bool] = False
    endswith_expression: ClassVar[str] = "{field} endswith {value}"
    not_endswith_expression: ClassVar[Optional[str]] = None
    endswith_expression_allow_special: ClassVar[bool] = False
    contains_expression: ClassVar[str] = "{field} contains {value}"
    not_contains_expression: ClassVar[Optional[str]] = None
    contains_expression_allow_special: ClassVar[bool] = False
    wildcard_match_expression: ClassVar[str] = (
        "{field} match {value}"  # Use if wildcards cannot be expressed with eq_token.
    )

    # Regular expressions
    re_expression: ClassVar[str] = "{field}=~{regex}"
    not_re_expression: ClassVar[Optional[str]] = None
    re_escape_char: ClassVar[str] = "\\"
    re_escape: ClassVar[Tuple[str]] = ()
    re_escape_escape_char: bool = True
    re_flag_prefix: bool = True
    re_flags: Dict[SigmaRegularExpressionFlag, str] = {
        SigmaRegularExpressionFlag.IGNORECASE: "i",
        SigmaRegularExpressionFlag.MULTILINE: "m",
        SigmaRegularExpressionFlag.DOTALL: "s",
    }

    # Case-sensitive string matching
    case_sensitive_match_expression: ClassVar[str] = "{field} casematch {value}"
    case_sensitive_startswith_expression: ClassVar[str] = (
        "{field} casematch_startswith {value}"
    )
    case_sensitive_not_startswith_expression: ClassVar[Optional[str]] = None
    case_sensitive_startswith_expression_allow_special: ClassVar[bool] = False
    case_sensitive_endswith_expression: ClassVar[str] = "{field} casematch_endswith {value}"
    case_sensitive_not_endswith_expression: ClassVar[Optional[str]] = None
    case_sensitive_endswith_expression_allow_special: ClassVar[bool] = False
    case_sensitive_contains_expression: ClassVar[str] = "{field} casematch_contains {value}"
    case_sensitive_not_contains_expression: ClassVar[Optional[str]] = None
    case_sensitive_contains_expression_allow_special: ClassVar[bool] = False

    # CIDR expressions
    cidr_expression: ClassVar[Optional[str]] = None
    not_cidr_expression: ClassVar[Optional[str]] = None

    # Numeric comparison operators
    compare_op_expression: ClassVar[str] = "{field}{operator}{value}"
    compare_operators: ClassVar[Dict[SigmaCompareExpression.CompareOperators, str]] = {
        SigmaCompareExpression.CompareOperators.LT: "<",
        SigmaCompareExpression.CompareOperators.LTE: "<=",
        SigmaCompareExpression.CompareOperators.GT: ">",
        SigmaCompareExpression.CompareOperators.GTE: ">=",
    }

    # Expression for comparing two event fields
    field_equals_field_expression: ClassVar[Optional[str]] = None
    field_equals_field_startswith_expression: ClassVar[Optional[str]] = None
    field_equals_field_endswith_expression: ClassVar[Optional[str]] = None
    field_equals_field_contains_expression: ClassVar[Optional[str]] = None
    field_timestamp_part_expression: ClassVar[Optional[str]] = None
    timestamp_part_mapping: ClassVar[Optional[Dict[SigmaTimestampPart, str]]] = None
    field_equals_field_escaping_quoting: Tuple[bool, bool] = (True, True)

    # Null/None expressions
    field_null_expression: ClassVar[str] = "{field} is null"

    # Field existence condition expressions
    field_exists_expression: ClassVar[str] = "exists({field})"
    field_not_exists_expression: ClassVar[str] = "notexists({field})"

    # Field value in list
    convert_or_as_in: ClassVar[bool] = True
    convert_and_as_in: ClassVar[bool] = True
    in_expressions_allow_wildcards: ClassVar[bool] = True
    field_in_list_expression: ClassVar[str] = "{field} {op} ({list})"
    or_in_operator: ClassVar[str] = "in"
    and_in_operator: ClassVar[str] = "contains-all"
    list_separator: ClassVar[str] = ", "

    # Value not bound to a field
    unbound_value_str_expression: ClassVar[str] = '"{value}"'
    unbound_value_num_expression: ClassVar[str] = "{value}"
    unbound_value_re_expression: ClassVar[str] = "_=~{value}"

    # Query finalization: appending and concatenating deferred query part
    deferred_start: ClassVar[str] = "\n| "
    deferred_separator: ClassVar[str] = "\n| "
    deferred_only_query: ClassVar[str] = "*"

    # Correlations
    # TODO: delete everything to the correlation end marker if correlations aren't implemented
    correlation_methods: ClassVar[Dict[str, str]] = {
        "default": "Test correlation method",
    }
    default_correlation_method: ClassVar[str] = "default"
    correlation_condition_mapping: ClassVar[
        Dict[SigmaCorrelationConditionOperator, str]
    ] = {
        SigmaCorrelationConditionOperator.LT: "<",
        SigmaCorrelationConditionOperator.LTE: "<=",
        SigmaCorrelationConditionOperator.GT: ">",
        SigmaCorrelationConditionOperator.GTE: ">=",
        SigmaCorrelationConditionOperator.EQ: "==",
        SigmaCorrelationConditionOperator.NEQ: "!=",
    }
    default_correlation_query: ClassVar[Dict[str, str]] = {
        "default": "{search}\n{aggregate}\n{condition}"
    }
    event_count_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    value_count_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    temporal_correlation_query: ClassVar[Dict[str, str]] = {
        "default": "{search}\n\n{aggregate}\n\n{condition}"
    }
    temporal_ordered_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    temporal_extended_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    temporal_ordered_extended_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    value_sum_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    value_avg_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    value_percentile_correlation_query: ClassVar[Optional[Dict[str, str]]] = None
    value_median_correlation_query: ClassVar[Optional[Dict[str, str]]] = None

    correlation_search_single_rule_expression: ClassVar[str] = "{query}"
    correlation_search_multi_rule_expression: ClassVar[str] = "{queries}"
    correlation_search_multi_rule_query_expression: ClassVar[
        str
    ] = 'subsearch (( {query} | set event_type="{ruleid}"{normalization} ))'
    correlation_search_multi_rule_query_expression_joiner: ClassVar[str] = "\n"
    typing_expression: ClassVar[Optional[str]] = None
    typing_rule_query_expression: ClassVar[Optional[str]] = None
    typing_rule_query_expression_joiner: ClassVar[Optional[str]] = None

    correlation_search_field_normalization_expression: ClassVar[str] = (
        " | set {alias}={field}"
    )
    correlation_search_field_normalization_expression_joiner: ClassVar[str] = ""

    event_count_aggregation_expression: ClassVar[Dict[str, str]] = {
        "default": "| aggregate window={timespan} count() as event_count{groupby}"
    }
    value_count_aggregation_expression: ClassVar[Dict[str, str]] = {
        "default": "| aggregate window={timespan} value_count({field}) as value_count{groupby}"
    }
    temporal_aggregation_expression: ClassVar[Dict[str, str]] = {
        "default": "| temporal window={timespan} eventtypes={referenced_rules}{groupby}"
    }
    temporal_ordered_aggregation_expression: ClassVar[Dict[str, str]] = {
        "default": "| temporal ordered=true window={timespan} eventtypes={referenced_rules}{groupby}"
    }
    temporal_extended_aggregation_expression: ClassVar[Optional[Dict[str, str]]] = None
    temporal_ordered_extended_aggregation_expression: ClassVar[
        Optional[Dict[str, str]]
    ] = None
    value_sum_aggregation_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_avg_aggregation_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_percentile_aggregation_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_median_aggregation_expression: ClassVar[Optional[Dict[str, str]]] = None

    timespan_mapping: ClassVar[Dict[str, str]] = {
        "m": "min",
    }
    timespan_seconds: ClassVar[bool] = False
    referenced_rules_expression: ClassVar[Dict[str, str]] = {"default": "{ruleid}"}
    referenced_rules_expression_joiner: ClassVar[Dict[str, str]] = {"default": ","}
    referenced_rules_plain_ruleid_pattern: ClassVar[Pattern] = re.compile(r"^[A-Za-z0-9_.\-]+$")

    groupby_expression: ClassVar[Dict[str, str]] = {"default": " by {fields}"}
    groupby_field_expression: ClassVar[Dict[str, str]] = {"default": "{field}"}
    groupby_field_expression_joiner: ClassVar[Dict[str, str]] = {"default": ", "}
    groupby_expression_nofield: ClassVar[Optional[Dict[str, str]]] = None

    correlation_fields_expression: ClassVar[Optional[Dict[str, str]]] = None
    correlation_fields_field_expression: ClassVar[Optional[Dict[str, str]]] = None
    correlation_fields_field_expression_joiner: ClassVar[Optional[Dict[str, str]]] = None

    event_count_condition_expression: ClassVar[Dict[str, str]] = {
        "default": "| where event_count {op} {count}"
    }
    value_count_condition_expression: ClassVar[Dict[str, str]] = {
        "default": "| where value_count {op} {count}"
    }
    temporal_condition_expression: ClassVar[Dict[str, str]] = {
        "default": "| where eventtype_count {op} {count}"
    }
    temporal_ordered_condition_expression: ClassVar[Dict[str, str]] = {
        "default": "| where eventtype_count {op} {count} and eventtype_order={referenced_rules}"
    }
    temporal_extended_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    temporal_ordered_extended_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_sum_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_avg_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_percentile_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    value_median_condition_expression: ClassVar[Optional[Dict[str, str]]] = None
    extended_correlation_condition_rule_reference_expression: ClassVar[Optional[str]] = None
    ### Correlation end ###

    # TODO: implement custom methods for query elements not covered by the default backend base.
    # Documentation: https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html

    {% if cookiecutter.additional_output_formats %}
    {% for format in cookiecutter.output_formats.split(",") %}
    def finalize_query_{{ format }}(
        self,
        rule: SigmaRule | SigmaCorrelationRule,
        query: str | DeferredQueryExpression,
        index: int,
        state: ConversionState,
    ) -> Any:
        # TODO: implement per-query output for format {{ format }}.
        return query

    def finalize_output_{{ format }}(self, queries: List[Any]) -> Any:
        # TODO: implement output finalization for format {{ format }}.
        return "\n".join(queries)
    {% endfor %}
    {% endif %}
