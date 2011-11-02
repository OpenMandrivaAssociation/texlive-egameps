Name:		texlive-egameps
Version:	1.1
Release:	1
Summary:	LaTeX package for typesetting extensive games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/egameps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egameps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egameps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The style is intended to have enough features to draw any
extensive game with relative ease. The facilities of PSTricks
are used for graphics. (An older version of the package, which
uses the LaTeX picture environment rather than PSTricks and
consequently has many fewer features is available on the
package home page.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/egameps/egameps.sty
%doc %{_texmfdistdir}/doc/latex/egameps/README
%doc %{_texmfdistdir}/doc/latex/egameps/egameps.pdf
%doc %{_texmfdistdir}/doc/latex/egameps/egameps.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
