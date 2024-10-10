- A new template named "styX" requires two new files 
  <styX.py> and <styX.css>

- To add any additional sections such as "projects, certificates, ...":
  create a generic function in mods.py w.r.t "writeSec" but independent of sty files
  call the generic function from style file 

- Follow the naming convention of: 
  "title", "org", "date", "highlights" 