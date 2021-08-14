import sys
import platform
import getpass
from types import SimpleNamespace
from datetime import datetime
from time import time, gmtime, strftime

from uceasy.facade import AssemblyFacade, QualityControlFacade, UCEPhylogenomicsFacade
from uceasy.tracking import save_tracking_file


tracking = {
    "Operating System": platform.platform(),
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "UCEasy command": "uceasy " + " ".join(sys.argv[1:]),
    "Who ran": getpass.getuser(),
}


def run_quality_control(context: SimpleNamespace):
    generate_log(context.log_dir)
    start_time = time()
    out = QualityControlFacade(context).run()
    tracking["Execution Time"] = strftime("%H:%M:%S", gmtime(time() - start_time))
    tracking["FASTQ"] = context.raw_fastq
    tracking["Standard output"] = out
    tracking["Commands"] = context.commands
    save_tracking_file(context.log_dir + "/" + context.tracking_file, tracking)


def run_assembly(context: SimpleNamespace):
    generate_log(context.log_dir)
    start_time = time()
    out = AssemblyFacade(context).run()
    tracking["Execution Time"] = strftime("%H:%M:%S", gmtime(time() - start_time))
    tracking["FASTQ"] = context.clean_fastq
    tracking["Standard output"] = out
    tracking["Commands"] = context.commands
    save_tracking_file(context.log_dir + "/" + context.tracking_file, tracking)


def run_phylogenomics(context: SimpleNamespace):
    generate_log(context.log_dir)
    start_time = time()
    out = UCEPhylogenomicsFacade(context).run()
    tracking["Execution Time"] = strftime("%H:%M:%S", gmtime(time() - start_time))
    tracking["FASTQ"] = context.contigs
    tracking["Standard output"] = out
    tracking["Commands"] = context.commands
    save_tracking_file(context.log_dir + "/" + context.tracking_file, tracking)
