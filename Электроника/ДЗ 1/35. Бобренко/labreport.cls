\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{labreport}[2021/05/04 BMST lab report]

\LoadClass[fontsize=14pt,openany]{scrbook}


% Поддержка русского языка
\RequirePackage[T2A]{fontenc}
\RequirePackage[russian]{babel}
\RequirePackage[utf8]{inputenc}

% Для эмблемы и вёрстки нназвания
\RequirePackage{graphicx}
\RequirePackage{tabularx, makecell}

% Параметры страницы
\RequirePackage{geometry}
\geometry{
    left = .5in,
    right = .5in,
    top = .5in,
    bottom = .5in,
    % head = 1cm,
    % foot = .5in,
}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1em}
\renewcommand{\baselinestretch}{.75}


% Переменные для настройки отображения
\newcommand*{\faculcy}[1]{\gdef\@faculcy{#1}}
\newcommand*{\@faculcy}{Информатика и системы управления}

\newcommand*{\descipline}[1]{\gdef\@descipline{#1}}
\newcommand*{\@descipline}{\#descipline\#}

\newcommand*{\cathedra}[1]{\gdef\@cathedra{#1}}
\newcommand*{\@cathedra}{Компьютерные системы и сети}

\newcommand*{\labRef}[1]{\gdef\@labRef{#1}}
\newcommand*{\@labRef}{\texttt{\#labRef\#}}

\newcommand*{\group}[1]{\gdef\@group{#1}}
\newcommand*{\@group}{ИУ6-\#group\#}

\subtitle{по лабораторной работе № \@labRef}

\author{\#author\#}

% Вспомогательные команды
\newcommand{\fillSpace}{\noindent\rule{5cm}{.5pt}}

\renewcommand{\maketitle}{
\begin{titlepage}
  
  
  \begin{center}
    {\footnotesize\bfseries
    Федеральное государственное бюджетное образовательное учреждение\\
    высшего профессионального образования
    }
  \end{center}
  
  
  \begin{tabularx}{\textwidth}{ >{\centering\arraybackslash}m{2.3cm} >{\centering\arraybackslash}m{2.3cm} }
    \includegraphics[width=2.034cm,height=2.305cm]{logo.png}
    
    &

    \makecell[c]{\itshape\bfseries
    «Московский государственный технический университет\\
    \itshape\bfseries имени Н.Э. Баумана»\\ 
    \\
    \itshape\bfseries (МГТУ им. Н.Э. Баумана)
    }
    
  \end{tabularx}
  \noindent\rule{\textwidth}{1pt}
  
  \vspace{.5cm}
  
  \begin{center}
    ФАКУЛЬТЕТ: \@faculcy
    
    КАФЕДРА: \@cathedra
  \end{center}
  

  \vfill
  

  \begin{center}    
    \textbf{\huge Отчёт}\\
    \textbf{\@subtitle}
  \end{center}
  
  \textbf{Название:} \@title
  
  \textbf{Дисциплина:} \@descipline
  

  \vfill
  
  
  \begin{tabularx}{\textwidth}{X c c} 
    
    Студент гр. \@group & \fillSpace & \@author \\
    & {\footnotesize (Подпись, дата)} & {\footnotesize (И.О. Фамилия)} \\ 
    
    Преподаватель & \fillSpace & В. А. Карпухин \\
    & {\footnotesize (Подпись, дата)} & {\footnotesize (И.О. Фамилия)} \\
  \end{tabularx}
  
  
  \vfill
  

  \begin{center}
    \small
    Москва, \the\year
  \end{center}
\end{titlepage}
}
