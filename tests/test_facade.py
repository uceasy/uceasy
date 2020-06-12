from types import SimpleNamespace


from uceasy.facade import QualityControlFacade, AssemblyFacade, UCEPhylogenomicsFacade


def test_quality_control_runs_sucessfully_with_illumiprocessor(context):
    ctx = SimpleNamespace(
        raw_fastq=context["raw_fastq"],
        csv_file=context["csv_file"],
        threads=1,
        single_end=False,
        single_index=False,
        r1_pattern=None,
        r2_pattern=None,
        phred64=True,
        output=context["output"] + "qc_facade",
        min_len=None,
        no_merge=False,
        capture_output=True,
    )
    facade = QualityControlFacade(ctx)
    output = facade.run()
    assert "Completed illumiprocessor" in str(output)


def test_assembly_runs_sucessfully_with_spades(context):
    ctx = SimpleNamespace(
        assembler="spades",
        clean_fastq=context["clean_fastq"],
        threads=1,
        output=context["output"] + "assembly_facade",
        config=None,
        kmer=None,
        no_clean=False,
        subfolder=None,
        capture_output=True,
    )
    facade = AssemblyFacade(ctx)
    output = facade.run()
    assert "Completed phyluce_assembly_assemblo_spades" in str(output)


def test_phylogenomics_runs_sucessfully(context):
    ctx = SimpleNamespace(
        aligner="mafft",
        charsets=True,
        contigs=context["contigs"],
        incomplete_matrix=True,
        internal_trimming=True,
        output=context["output"] + "phylogenomics_facade",
        log_dir="",
        probes=context["probes"],
        percent=0.75,
        threads=1,
        regex=None,
        capture_output=True,
    )
    facade = UCEPhylogenomicsFacade(ctx)
    output = str(facade.run())
    assert "Completed phyluce_assembly_match_contigs_to_probes" in output
    assert "Completed phyluce_assembly_get_match_counts" in output
    assert "Completed phyluce_assembly_get_fastas_from_match_counts" in output
    assert "Completed phyluce_align_seqcap_align" in output
    assert "Completed phyluce_align_get_gblocks_trimmed_alignments_from_untrimmed" in output
    assert "Completed phyluce_align_remove_locus_name_from_nexus_lines" in output
    assert "Completed phyluce_align_get_only_loci_with_min_taxa" in output
    assert "Completed phyluce_align_format_nexus_files_for_raxml" in output
