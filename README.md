# 项目结构
```text
ShuThesis/
├── .git/ (Git仓库目录)
├── .gitignore (4.8KB)
├── .python-version (0.0KB)
├── .run/ (PyCharm运行配置目录)
├── README.md (0.5KB)
├── pyproject.toml (0.3KB)
├── uv.lock (262.1KB)
├── paper/ (论文模板目录)
│   ├── README.md (1.4KB)
│   ├── cover.pdf (724.4KB)
│   ├── data/ (论文章节数据目录)
│   │   ├── abstract.tex (0.3KB)
│   │   ├── acknowledgement.tex (0.2KB)
│   │   ├── appendix.tex (0.9KB)
│   │   ├── chap01.tex (4.0KB)
│   │   ├── chap02.tex (1.3KB)
│   │   ├── chap03.tex (2.3KB)
│   │   ├── chap04.tex (1.1KB)
│   │   └── test.tex (0.3KB)
│   ├── dtx-style.sty (4.4KB)
│   ├── figures/ (论文图片目录)
│   │   ├── shu.pdf (4.9KB)
│   │   ├── shublack.pdf (4.9KB)
│   │   ├── shulogo.pdf (18.6KB)
│   │   ├── shulogo.png (59.2KB)
│   │   └── shulogoblack.pdf (18.6KB)
│   ├── main.tex (1.5KB)
│   ├── make-doc.bat (0.4KB)
│   ├── out/ (输出目录)
│   ├── reference/ (参考文献目录)
│   │   └── refs.bib (2.7KB)
│   ├── shuthesis.bst (56.1KB)
│   ├── shuthesis.cfg (2.9KB)
│   ├── shuthesis.cls (22.7KB)
│   ├── shuthesis.dtx (73.0KB)
│   ├── shuthesis.ins (2.7KB)
│   ├── shuthesis.pdf (404.9KB)
│   └── shuthesis.sty (0.6KB)
└── project/ (Python项目目录)
    ├── __init__.py (0.0KB)
    └── main.py (0.1KB)
```


# LaTeX 论文部分

本模板由 [Overleaf 上 SHUOSC](https://www.overleaf.com/latex/templates/shu-bachelor-thesis-osc-master/ygndtxdbqnyf) 的模板改进而来，更改了一些格式上的问题，以符合最新要求。

模板可能还有一些问题，如摘要字体等。

编译方法：`pdfLaTeX -> BibTeX -> pdfLaTeX -> pdfLaTeX`。如果是JetBrains编辑器的话应该可以直接使用`.run/`下的两个配置文件。

论文输出目录在 `out/` 下。

# Python开发部分

推荐使用 uv 管理 Python 环境。

可以使用 Python 进行开发，输出内容可以直接指定到论文文件夹。