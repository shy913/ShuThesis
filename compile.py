#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
from tqdm import tqdm

def run_command(cmd, cwd=None, description="", allow_retcodes=None, env=None):
    """
    执行外部命令，实时打印输出，并返回是否成功。
    显式指定 UTF-8 编码，避免 GBK 解码错误。
    """
    if allow_retcodes is None:
        allow_retcodes = {0}
    print(f"\n{'='*60}\n执行命令: {' '.join(cmd)}\n描述: {description}\n{'='*60}")
    process_env = os.environ.copy()
    if env:
        process_env.update(env)
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=cwd,
        env=process_env,
        text=True,
        encoding='utf-8',
        errors='replace',
        bufsize=1
    )

    for line in process.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()

    retcode = process.wait()
    if retcode not in allow_retcodes:
        print(f"\n命令执行失败，返回码 {retcode}")
        return False
    return True

def compile_latex(project_dir, main_file="main"):
    """
    在 project_dir 中编译 LaTeX 文档。
    main_file 是不带 .tex 扩展名的文件名。

    pdflatex -interaction=nonstopmode 即使成功输出 PDF，
    也可能因非致命错误返回非零退出码。因此允许返回码 {0, 1}。
    fontgen_dir = os.path.join(os.path.dirname(project_dir), "fontgen")
    if os.path.isdir(fontgen_dir):
        sep = ";" if sys.platform == "win32" else ":"
        old_texinputs = os.environ.get("TEXINPUTS", "")
        texinputs = f"{fontgen_dir}//{sep}{old_texinputs}"
        latex_env = {"TEXINPUTS": texinputs}
    else:
        latex_env = None

    steps = [
        (["pdflatex", "-interaction=nonstopmode", main_file],
         "第一次 pdflatex 编译", {0, 1}),
        (["bibtex", main_file],
         "BibTeX 处理参考文献", {0, 1}),
        (["pdflatex", "-interaction=nonstopmode", main_file],
         "第二次 pdflatex 编译 (解决引用)", {0, 1}),
        (["pdflatex", "-interaction=nonstopmode", main_file],
         "第三次 pdflatex 编译 (最终版本)", {0, 1}),
    ]

    with tqdm(total=len(steps), desc="LaTeX 编译进度", unit="step", ncols=80) as pbar:
        for cmd, desc, allow_retcodes in steps:
            pbar.set_description(f"正在执行: {desc}")
            success = run_command(cmd, cwd=project_dir, description=desc,
                                  allow_retcodes=allow_retcodes, env=latex_env)
            if not success:
                print(f"\n❌ 编译失败，停止于步骤: {desc}")
                sys.exit(1)
            pbar.update(1)

    print("\n✅ 所有编译步骤成功完成！")

if __name__ == "__main__":
    base_dir = os.getcwd()
    paper_dir = os.path.join(base_dir, "paper")

    if not os.path.isdir(paper_dir):
        print(f"错误：找不到目录 {paper_dir}")
        sys.exit(1)

    compile_latex(paper_dir, main_file="main")
