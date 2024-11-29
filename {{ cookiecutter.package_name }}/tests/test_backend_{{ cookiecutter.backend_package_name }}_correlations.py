import pytest
from sigma.collection import SigmaCollection
from sigma.backends.{{ cookiecutter.backend_package_name }} import {{ cookiecutter.backend_class_name }}
from tests.test_backend_{{ cookiecutter.backend_package_name }} import {{ cookiecutter.backend_package_name }}_backend

# Correlation tests - delete whole file if your backend doesn't supports correlation rules.
def test_event_count_correlation_rule_stats_query({{ cookiecutter.backend_package_name }}_backend : {{ cookiecutter.backend_class_name }}):
    correlation_rule = SigmaCollection.from_yaml(
        """
title: Base rule
name: base_rule
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value1
        fieldB: value2
    condition: selection
---
title: Multiple occurrences of base event
status: test
correlation:
    type: event_count
    rules:
        - base_rule
    group-by:
        - fieldC
        - fieldD
    timespan: 15m
    condition:
        gte: 10
            """
    )
    assert {{ cookiecutter.backend_package_name }}_backend.convert(correlation_rule) == [
        """Expected result"""
    ]

def test_value_count_correlation_rule_stats_query({{ cookiecutter.backend_package_name }}_backend):
    correlation_rule = SigmaCollection.from_yaml(
        """
title: Base rule
name: base_rule
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value1
        fieldB: value2
    condition: selection
---
title: Multiple occurrences of base event
status: test
correlation:
    type: value_count
    rules:
        - base_rule
    group-by:
        - fieldC
    timespan: 15m
    condition:
        lt: 10
        field: fieldD
            """
    )
    assert {{ cookiecutter.backend_package_name }}_backend.convert(correlation_rule) == [
        """Expected result"""
    ]

def test_temporal_correlation_rule_stats_query({{ cookiecutter.backend_package_name }}_backend):
    correlation_rule = SigmaCollection.from_yaml(
        """
title: Base rule 1
name: base_rule_1
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value1
        fieldB: value2
    condition: selection
---
title: Base rule 2
name: base_rule_2
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value3
        fieldB: value4
    condition: selection
---
title: Temporal correlation rule
status: test
correlation:
    type: temporal
    rules:
        - base_rule_1
        - base_rule_2
    aliases:
        field:
            base_rule_1: fieldC
            base_rule_2: fieldD
    group-by:
        - fieldC
    timespan: 15m
"""
    )
    assert {{ cookiecutter.backend_package_name }}_backend.convert(correlation_rule) == [
        """Expected result"""
    ]

def test_temporal_ordered_correlation_rule_stats_query({{ cookiecutter.backend_package_name }}_backend):
    correlation_rule = SigmaCollection.from_yaml(
        """
title: Base rule 1
name: base_rule_1
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value1
        fieldB: value2
    condition: selection
---
title: Base rule 2
name: base_rule_2
status: test
logsource:
    category: test
detection:
    selection:
        fieldA: value3
        fieldB: value4
    condition: selection
---
title: Ordered temporal correlation rule
status: test
correlation:
    type: temporal_ordered
    rules:
        - base_rule_1
        - base_rule_2
    aliases:
        field:
            base_rule_1: fieldC
            base_rule_2: fieldD
    group-by:
        - fieldC
    timespan: 15m
"""
    )
    assert {{ cookiecutter.backend_package_name }}_backend.convert(correlation_rule) == [
        """Expected result"""
    ]