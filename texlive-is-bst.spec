Name:		texlive-is-bst
Version:	52623
Release:	2
Summary:	Extended versions of standard BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/is-bst
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/is-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/is-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains an extended version (xbtxbst.doc) of the
source of the standard BibTeX styles, together with
corresponding versions of the standard styles. The styles offer
support for CODEN, ISBN, ISSN, LCCN, and PRICE fields, extended
PAGES fields, the PERIODICAL entry, and extended citation label
suffixing.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/is-bst
%doc %{_texmfdistdir}/doc/bibtex/is-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
