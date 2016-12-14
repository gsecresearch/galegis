#http://media.ethics.ga.gov/Search/Lobbyist/Lobbyist_ByName.aspx
CLQuery<- 
  function(lastname=NULL, firstname=NULL, city=NULL,year=2016) { library(XML)
  full_url<- paste("http://media.ethics.ga.gov/Search/Lobbyist/Lobbyist_results.aspx?&Year=",year,"&LastName=",lastname,"&FirstName=",firstname,"&City=",city,"&FilerID=",sep="")
   html_result<- readHTMLTable(full_url)
extractLobbyist<- html_result$ctl00_ContentPlaceHolder1_Results$Lobbyist
extractAddress<- html_result$ctl00_ContentPlaceHolder1_Results$Address

rettt<- data.frame(Lobbyist_Name=extractLobbyist,Lobbyist_Address=extractAddress)
lll<- list(Lobbyist_Info=rettt,Query=full_url,Full_HTML=html_result)
lll
  }







