import os
import subprocess
import glob

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def compile_tex():
    # Change context to the report directory exactly where this script lives
    report_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(report_dir)
    
    tex_file = "GIC_Report.tex"
    base_name = "GIC_Report"

    print("Generating PDF Report. Please wait...\n")
    
    try:
        # Run standard LaTeX compilation chain for bibliography and Table of Contents
        run_command(["pdflatex", "-interaction=nonstopmode", tex_file])
        run_command(["bibtex", base_name])
        run_command(["pdflatex", "-interaction=nonstopmode", tex_file])
        run_command(["pdflatex", "-interaction=nonstopmode", tex_file])
        
        print("\nCompilation finished successfully. Cleaning up auxiliary files...")
        
        exts_to_delete = ["*.aux", "*.log", "*.toc", "*.bbl", "*.blg", "*.out", "*.lof"]
        for ext in exts_to_delete:
            for file_path in glob.glob(os.path.join(report_dir, ext)):
                try:
                    os.remove(file_path)
                    print(f"  Deleted: {os.path.basename(file_path)}")
                except Exception as e:
                    print(f"  Failed to delete {file_path}: {e}")
        
        print("\nDone! Check your final file: GIC_Report.pdf")

    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] compilation failed at: {' '.join(e.cmd)}")
        print("Please ensure pdflatex and bibtex are installed on your Linux system.")
        print("(e.g., `sudo apt install texlive-full` or similar)")

if __name__ == "__main__":
    compile_tex()
