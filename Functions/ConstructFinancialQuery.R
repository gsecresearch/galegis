#This queries the State Ethics Commission's Personal financial search.  You can search
#By last name, first name, or filer id, but I didn't write that in because I don't know what those are.
ConstructFinancialQuery<- 
  function(lastname=NULL, firstname=NULL, city=NULL)   { 
  library(XML)
  full_url<- paste("http://media.ethics.ga.gov/search/Financial/Financial_BYNameResults.aspx?LastName=",lastname,"&FirstName=",firstname,"&City=",city,"&FilerID=&OfficeStatus=0&OfficeName=&District=&Post=&Circuit=&Division=&Type=Name",sep="")
   html_result<- readHTMLTable(full_url)
  html_result}



#ENHANCEMENTS: / Automatically read in the file and give the user a table of names and addresses.
#Construct personal financial query.  
CPFQuery<- 
  function(lastname=NULL, firstname=NULL, city=NULL)   { 
  library(XML)
  full_url<- paste("http://media.ethics.ga.gov/search/Financial/Financial_BYNameResults.aspx?LastName=",lastname,"&FirstName=",firstname,"&City=",city,"&FilerID=&OfficeStatus=0&OfficeName=&District=&Post=&Circuit=&Division=&Type=Name",sep="")
   html_result<- readHTMLTable(full_url)
extractFiler<- html_result$ctl00_ContentPlaceHolder1_GridView1$Filer
extractAddress<- html_result$ctl00_ContentPlaceHolder1_GridView1$Address
exf2<- html_result[[6]]$V2
exa2<- html_result[[6]]$V3

rettt<- data.frame(Filer1=extractFiler,Filer2=extractAddress)
rett2<- data.frame(Filer1=exf2,Filer2=exa2)
returna<- list(Return_1=rettt,Return_2=rett2,Full_HTML=html_result)
returna
   }


