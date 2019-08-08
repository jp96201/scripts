function(DP1,DP2,mu,se,type,lefttail){
  plot_area <- function(min,max,mu,se)
  {
    function(x)
    {
      y <- dnorm(x,mean=mu, sd=se)
      y[x<min | x>max] <-NA
      return(y)
    }
  }#draw normal distribution in specific area
  #draw hypothesis testing plot
  library(ggplot2)
  if(type=="s1t2"||type=="s1t2p"||type=="s2pair"||type=="s2pair0"){
    plot<-ggplot(data.frame(x=c(mu-4*se,mu+4*se)), aes(x=x))+
      theme_bw()+
      stat_function(fun=plot_area(mu-4*se,DP1,mu,se), geom="area", fill="red", alpha=0.3)+
      stat_function(fun=plot_area(DP2,mu+4*se,mu,se), geom="area", fill="red", alpha=0.3)+
      stat_function(fun=plot_area(DP1,DP2,mu,se), geom="area", fill="green", alpha=0.3)+
      stat_function(fun=dnorm, args = list(mean=mu,sd=se))+
      geom_text(aes(y=0, x=c(DP1),label=paste("x1=",c(round(DP1,3)))))+
      geom_text(aes(y=0, x=c(DP2),label=paste("x2=",c(round(DP2,3)))))
    plot+labs(title=paste("Standard error:",se))
  }else if(type=="s1t1"||type=="s1t1p"){
    if(lefttail==1){
      plot<-ggplot(data.frame(x=c(mu-4*se,mu+4*se)), aes(x=x))+
        theme_bw()+
        stat_function(fun=plot_area(mu-4*se,DP1,mu,se), geom="area", fill="green", alpha=0.3)+
        stat_function(fun=plot_area(DP1,mu+4*se,mu,se), geom="area", fill="red", alpha=0.3)+
        stat_function(fun=dnorm, args = list(mean=mu,sd=se))+
        geom_text(aes(y=0, x=c(DP1),label=paste(c(round(DP1,3)))))
    }else if(lefttail==0){
      plot<-ggplot(data.frame(x=c(mu-4*se,mu+4*se)), aes(x=x))+
        theme_bw()+
        stat_function(fun=plot_area(DP2,mu+4*se,mu,se), geom="area", fill="green", alpha=0.3)+
        stat_function(fun=plot_area(mu-4*se,DP2,mu,se), geom="area", fill="red", alpha=0.3)+
        stat_function(fun=dnorm, args = list(mean=mu,sd=se))+
        geom_text(aes(y=0, x=c(DP2),label=paste(c(round(DP2,3)))))
    }else{
      print("Wrong argument for lefttail!")
    }
    plot+labs(title=paste("Standard error:",se))
  }
}
