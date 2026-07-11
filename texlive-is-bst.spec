%global tl_name is-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.03
Release:	%{tl_revision}.1
Summary:	Extended versions of standard BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/is-bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/is-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/is-bst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains an extended version (xbtxbst.doc) of the source of
the standard BibTeX styles, together with corresponding versions of the
standard styles. The styles offer support for CODEN, ISBN, ISSN, LCCN,
and PRICE fields, extended PAGES fields, the PERIODICAL entry, and
extended citation label suffixing.

