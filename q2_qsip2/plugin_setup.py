# ----------------------------------------------------------------------------
# Copyright (c) 2024, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from qiime2.plugin import Citations, Float, Int, List, Metadata, Plugin, Str
from q2_types.feature_table import FeatureTable, Frequency

from q2_qsip2 import __version__
from q2_qsip2.types import QSIP2Data, Unfiltered, Filtered, EAF
from q2_qsip2.workflow import (
    standard_workflow, create_qsip_data, subset_and_filter,
    resample_and_calculate_EAF
)
from q2_qsip2.visualizers._visualizers import (
    plot_weighted_average_densities, plot_sample_curves, plot_density_outliers,
    show_comparison_groups, plot_filtered_features, plot_excess_atom_fractions
)


citations = Citations.load("citations.bib", package="q2_qsip2")

plugin = Plugin(
    name="qsip2",
    version=__version__,
    website="www.qiime2.org",
    package="q2_qsip2",
    description=(
        "A plugin for analyzing quantitative stable isotope probing (qSIP) "
        "data."
    ),
    short_description="Analyze qSIP data.",
    citations=[citations['Caporaso-Bolyen-2024']]
)

plugin.methods.register_function(
    function=create_qsip_data,
    inputs={
        'table': FeatureTable[Frequency]
    },
    parameters={
        'sample_metadata': Metadata,
        'source_metadata': Metadata,
        'source_mat_id_column': Str,
        'isotope_column': Str,
        'isotopolog_column': Str,
        'gradient_position_column': Str,
        'gradient_pos_density_column': Str,
        'gradient_pos_amt_column': Str,
    },
    outputs=[
        ('qsip_data', QSIP2Data[Unfiltered])
    ],
    input_descriptions={
        'table': 'The qSIP feature table.'
    },
    parameter_descriptions={
        'sample_metadata': 'The sample-level metadata.',
        'source_metadata': 'The source-level metadata.',
        'source_mat_id_column': 'The name of the source id column.',
        'isotope_column': 'The name of the isotope column.',
        'isotopolog_column': 'The name of the isotopolog column.',
        'gradient_position_column': 'The name of the gradient position column.',
        'gradient_pos_density_column': 'The name of the density column.',
        'gradient_pos_amt_column': 'The name of the amount column.',
    },
    output_descriptions={
        'qsip_data': 'Placeholder.'
    },
    name='Bundle your qSIP metadata and feature table.',
    description=(
        'Placeholder.'
    ),
    citations=[]
)

plugin.methods.register_function(
    function=subset_and_filter,
    inputs={
        'qsip_data': QSIP2Data[Unfiltered]
    },
    parameters={
        'unlabeled_sources': List[Str],
        'labeled_sources': List[Str],
        'min_unlabeled_sources': Int,
        'min_labeled_sources': Int,
        'min_unlabeled_fractions': Int,
        'min_labeled_fractions': Int
    },
    outputs=[
        ('filtered_qsip_data', QSIP2Data[Filtered])
    ],
    input_descriptions={
        'qsip_data': 'Your unfiltered qSIP2 data.'
    },
    parameter_descriptions={
        'unlabeled_sources': 'The IDs of the unlabeled sources to retain.',
        'labeled_sources': 'The IDs of the labeled sources to retain.',
        'min_unlabeled_sources': (
            'The minimum number of unlabeled sources a feature must be '
            'present in to be retained.'
        ),
        'min_labeled_sources': (
            'The minimum number of labeled sources a feature must be present '
            'in to be retained.'
        ),
        'min_unlabeled_fractions': (
            'The minimum number of fractions a feature must be present in '
            'to be considered present in an unlabeled source.'
        ),
        'min_labeled_fractions': (
            'The minimum number of fractions a feature must be present in '
            'to be considered present in a labeled source.'
        )
    },
    output_descriptions={
        'filtered_qsip_data': 'Your subsetted and filtered qSIP2 data.'
    },
    name='Subset sources and filter features to prepare for comparison.',
    description=(
        'Placeholder.'
    ),
    citations=[]
)

plugin.methods.register_function(
    function=resample_and_calculate_EAF,
    inputs={
        'filtered_qsip_data': QSIP2Data[Filtered]
    },
    parameters={
        'resamples': Int,
        'random_seed': Int,
    },
    outputs=[
        ('eaf_qsip_data', QSIP2Data[EAF])
    ],
    input_descriptions={
        'filtered_qsip_data': 'Your filtered qSIP2 data.'
    },
    parameter_descriptions={
        'resamples': 'The number of bootstrap resamplings to perform.',
        'random_seed': 'The random seed to use during resampling.',
    },
    output_descriptions={
        'eaf_qsip_data': (
            'Your qSIP2 data with excess atom fraction (EAF) values '
            'calculated on a per-taxon basis.'
        )
    },
    name='Calculate excess atom fraction (EAF).',
    description=(
        'Placeholder.'
    ),
    citations=[]
)

plugin.visualizers.register_function(
    function=plot_weighted_average_densities,
    inputs={
        'qsip_data': QSIP2Data[Unfiltered]
    },
    parameters={
        'group': Str
    },
    input_descriptions={
        'qsip_data': 'The qSIP data for which to plot the weighted average '
                     'densities.'
    },
    parameter_descriptions={
        'group': 'A source-level metadata column used to facet the plot.'
    },
    name='Plot weighted average densities.',
    description=(
        'Plots the per-source weighted average density, colored by isotope '
        'and optionally faceted by the source-level metadata column `group`.'
    ),
    citations=[],
)

plugin.visualizers.register_function(
    function=plot_sample_curves,
    inputs={
        'qsip_data': QSIP2Data[Unfiltered]
    },
    parameters={},
    input_descriptions={
        'qsip_data': 'The qsip data artifact.'
    },
    parameter_descriptions={},
    name='Plot per-source density curves.',
    description=(
        'Plots gradient position by relative amount of DNA, faceted by source.'
    ),
    citations=[],
)

plugin.visualizers.register_function(
    function=plot_density_outliers,
    inputs={
        'qsip_data': QSIP2Data[Unfiltered]
    },
    parameters={},
    input_descriptions={
        'qsip_data': 'The qsip data artifact.'
    },
    parameter_descriptions={},
    name='Plot per-source density outliers.',
    description=(
        'Plots gradient position by density, faceted by source, and performs '
        'Cook\'s outlier detection.'
    ),
    citations=[],
)

plugin.visualizers.register_function(
    function=show_comparison_groups,
    inputs={
        'qsip_data': QSIP2Data[Unfiltered]
    },
    parameters={
        'groups': List[Str]
    },
    input_descriptions={
        'qsip_data': 'The qsip data artifact.'
    },
    parameter_descriptions={
        'groups': 'The names of one or more source-level metadata columns used '
                  'to further subdivide the labeled and unlabeled samples.'
    },
    name='Show available comparison groupings.',
    description=(
        'Displays a table of source-level ids grouped in columns by isotope '
        'and in rows by the given groups.'
    ),
    citations=[],
)

plugin.visualizers.register_function(
    function=plot_filtered_features,
    inputs={
        'filtered_qsip_data': QSIP2Data[Filtered]
    },
    parameters={},
    input_descriptions={
        'filtered_qsip_data': 'Your filtered qsip data artifact.'
    },
    parameter_descriptions={},
    name='Visualize feature retention.',
    description=(
        'Displays per-source stacked bar charts of feature retention by '
        'relative abundance and feature count.'
    ),
    citations=[],
)

plugin.visualizers.register_function(
    function=plot_excess_atom_fractions,
    inputs={
        'eaf_qsip_data': QSIP2Data[EAF],
    },
    parameters={
        'num_top': Int,
        'confidence_interval': Float
    },
    input_descriptions={
        'eaf_qsip_data': 'Your EAF-calculated qSIP2 data.',
    },
    parameter_descriptions={
        'num_top': (
            'The number of taxa displayed, selected in order of decreasing '
            'excess atom fraction.'
        ),
        'confidence_interval': (
            'The confidence interval to display from the bootstrapped excess '
            'atom fractions.'
        )
    },
    name='Visualize per-taxon excess atom fractions.',
    description=(
        'Plots per-taxon excess atom fractions with bootstrapped confidence '
        'intervals.'
    ),
    citations=[]
)

importlib.import_module('q2_qsip2.types._deferred_setup')
