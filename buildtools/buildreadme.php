<?php
$source=file_get_contents("Alembic.tex");
$matches=[];
preg_match_all('/
    (?|             # two alternatives whose group numbers both begin at 1
      \\\\chapter  # match the command
      (?|\{([^}]*)\}|\[([^]]*)\])
                    # and a parameter in group 1
    |               # OR
      \G            # anchor the match to the end of the last match
      (?|\{([^}]*)\}|\[([^]]*)\])
                    # and match a parameter in group 1
    )
    /x',
    $source,
    $matches
);
$poems=$matches[1];
$endB="";
$f=file("README.md");
$writeStuff=true;
foreach($f as $line){
        if(trim($line)=="<!-- BEGIN POEMLIST -->"){
                $writeStuff=false;
                $endB.=$line;
                foreach($poems as $p) $endB.="* ".$p."\n";
        }
        if($writeStuff) $endB.=$line;
        if(trim($line)=="<!-- END POEMLIST -->"){
                $endB.=$line;
                $writeStuff=true;
        }
}

file_put_contents("README.md",$endB);

