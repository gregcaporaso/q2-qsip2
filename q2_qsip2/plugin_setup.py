# ----------------------------------------------------------------------------
# Copyright (c) 2024, Colin Wood.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Bool, Citations, Metadata, Plugin, Str
from q2_types.feature_table import FeatureTable, Frequency

from q2_qsip2 import __version__
from q2_qsip2.workflow import standard_workflow


citations = Citations.load("citations.bib", package="q2_qsip2")

plugin = Plugin(
    name="qsip2",
    version=__version__,
    website="www.qiime2.org",
    package="q2_qsip2",
    description="A plugin for analyzing quantitative stable isotope probing (qSIP) data.",
    short_description="Analyze qSIP data.",
    # TODO
    citations=[citations['Caporaso-Bolyen-2024']]
)

plugin.methods.register_function(
    function=standard_workflow,
    inputs={
        'table': FeatureTable[Frequency],
    },
    parameters={
        'sample_metadata': Metadata,
        'source_metadata': Metadata,
        'split_metadata': Bool,
        'source_mat_id_column': Str,
        'isotope_column': Str,
        'isotopolog_column': Str,
        'gradient_position_column': Str,
        'gradient_position_density_column': Str,
        'gradient_position_amount_column': Str,
    },
    outputs=[
        ('output_table', FeatureTable[Frequency])
    ],
    input_descriptions={
        # TODO: more detail
        'table': 'The feature table.',
    },
    parameter_descriptions={
        # TODO: more detail
        'sample_metadata': 'The sample-level metadata.',
        'source_metadata': 'The source-level metadata.',
        'split_metadata': 'Whether to extract source-level metadata.',
        'source_mat_id_column': 'The name of the source id column.',
        'isotope_column': 'The name of the isotope column.',
        'isotopolog_column': 'The name of the isotopolog column.',
        'gradient_position_column': 'The name of the gradient position column.',
        'gradient_position_density_column': 'The name of the density column.',
        'gradient_position_amount_column': 'The name of the amount column.',
    },
    output_descriptions={
        # TODO: more detail
        'output_table': 'Placeholder.'
    },
    name='Run the standard qSIP2 workflow.',
    description=(
        # TODO: more detail
        'Placeholder.'
    ),
)
