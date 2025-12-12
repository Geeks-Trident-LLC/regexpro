"""Top-level module for regexgenerator.

- support TextPattern, ElementPattern, LinePattern, MultilinePattern, and PatternBuilder
- support predefine pattern reference on system_references.yaml
- allow end-user to customize pattern on /home/.geekstrident/regexgenerator/user_references.yaml
- allow end-user to generate test script or pattern on GUI application.
- dynamically generate Python snippet script
- dynamically generate Python unittest script
- dynamically generate Python pytest script
"""

from regexgenerator.collection import TextPattern
from regexgenerator.collection import ElementPattern
from regexgenerator.collection import LinePattern
from regexgenerator.collection import PatternBuilder
from regexgenerator.collection import MultilinePattern
from regexgenerator.collection import PatternReference
from regexgenerator.core import RegexBuilder
from regexgenerator.core import DynamicTestScriptBuilder
from regexgenerator.core import add_reference
from regexgenerator.core import remove_reference

from regexgenerator.core import NonCommercialUseCls

from regexgenerator.config import version
from regexgenerator.config import edition
__version__ = version
__edition__ = edition

__all__ = [
    'TextPattern',
    'ElementPattern',
    'LinePattern',
    'MultilinePattern',
    'PatternBuilder',
    'PatternReference',
    'RegexBuilder',
    'DynamicTestScriptBuilder',
    'NonCommercialUseCls',
    'add_reference',
    'remove_reference',
    'version',
    'edition',
]
