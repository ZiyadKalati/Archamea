/*
 * First you get all the sections that carry the articles for short stories,
 * biographies, and non-fiction. Each of these sections has a class with value
 * "the-articles".
 */
    var $otherArticlesSections = $(".the-articles");
    
/*
 * Add an event listener to the navigation bar for the "other articles". Because
 * of event bubbling, the event will still be triggered when clicking on the
 * "buttons" (list items) in the navigation bar. You find which was clicked with
 * .target and make another jQuery object for it and cache it.
 *
 * Another thing is to create options list to allow visitors to choose whether to
 * have one, two or three lists for the three types of articles available at the
 * same time. This list is created with the value "options" as it's class and then
 * appended to DOM.
 */
 
      var $otherArticlesNav = $(".other-articles nav li");
      
      var $options = $("<span class='options'>\
		  			 <li class='active'>One</li>\
					 <li>Two</li>\
					 <li>Three</li>\
					 <li>Four</li></span>");

	  $otherArticlesNav.parent().append($options);
	
/*
 * Check if target is the current active tab; if not then run block of code to change
 * the active tab and also the content that is shown on the page. First you filter
 * select the children of the children of the navigation bar (ul then li), then loop
 * through each li element and check if they have .current as a class value. If yes,
 * then run block of code and remove that class value and hide the entire section of
 * articles. Then you show the selected section of articles by using the .index
 * method, which finds the index of selected element or object relative to its
 * siblings if it has any. Then finally you add the class value to the clicked on tab
 * and return false to end the loop. Since you found the clicked on tab and changed
 * the content of the page already then you don't need to loop through each li
 * element anymore.
 */
      $otherArticlesNav.on("click", function(event){
	    var $target = $(event.target);
	  
	    if (!$target.is(".current") && !$target.parent().is(".options"))
	    { 
	      $otherArticlesNav.each(function(index){
	        var $this = $(this);
	        if ($this.is(".current"))
	        {
	          $this.removeClass("current");
  	          $otherArticlesSections.eq(index).hide();

		      $otherArticlesSections.eq($target.index()).fadeIn(350);	        
		      $target.addClass("current");

	          return false;
	        }
	      });  
	    }
	  }); // End of event listener

   
    var width = $otherArticlesSections.eq(0).css("width").replace("px", "");
    var currentIndex = 0;

	$options.on("click", "li", function(event){
	  var $target = $(event.target);
	  
	  if (!$target.is(".current"))
	  {
   	    var $optionsChildren = $options.children();
        var $targetIndexPlusOne = $target.index() + 1;
        var resizeFactor = Math.abs((currentIndex - $target.index()) * 2) + "px";
	    
	    var widthAdjust = ($target.index() * 10) / $targetIndexPlusOne;
	    articleGridWidth = Math.floor(width / ($targetIndexPlusOne)) - widthAdjust;
	    
		$optionsChildren.filter(".current").removeClass("current");
	    $target.addClass("current");
	    
	    $otherArticlesNav.slice(0, $targetIndexPlusOne).addClass("current");
	    $otherArticlesNav.slice($targetIndexPlusOne).removeClass("current");
	      
	      if ($target.index() > currentIndex)
	      {
	        $otherArticlesSections.slice(0, $targetIndexPlusOne)
	        					  .animate({
	        					    width: articleGridWidth
	        					  }, 150)
	        					  .css({display: "block", marginRight: "10px"});
			
			$otherArticlesSections.css({fontSize: "-=" + resizeFactor});
			
	      	$otherArticlesSections.slice(1, $targetIndexPlusOne)
	      	  					  .not(".shown")
	      	  					  .css({opacity: "0.0", left: "50%", width: articleGridWidth})
	      	  					  .addClass("shown")
								  .animate({
 		      					    left: "-=50%",
 		      					    opacity: "1.0"
	  	    					  }, 150);
	  	  }
	  	  else
	  	  {
	  	    var hasExecuted = false;
	  	    
    		$otherArticlesSections.slice($targetIndexPlusOne)
    							  .animate({
          						    left: "+=50%",
          						    opacity: "0.0"
          						  }, 150, function(){
          						    $(this)
	      						      .css({left: "0%",
	      						      		display: "none",
	      						      		marginRight: "0px",
	      						      		opacity: "1.0",
	      						      		width: articleGridWidth
	      						      		})
	      						      	.removeClass("shown");
	      						      
	  	     					    $otherArticlesSections.filter(".shown")
	  	     					    					  .animate({
	  	     					    					    width: articleGridWidth
	  	     					    					  }, 150, function(){
	  	     					    					    if (!hasExecuted)
	  	    					                          	{
	  	    					      						  $otherArticlesSections.css({fontSize: "+=" + resizeFactor});
	  	    					      						  hasExecuted = true;
	  	    					     						}
  	  	     					    					  });
	      						  });
	  	  }
	    
	    currentIndex = $target.index();
	  }  
	}); // End of event listener

/*    
    var clickerButton1 = $(".short-story").eq(1);
    var clickerButton2 = $(".biography").eq(1);
    var clickerButton3 = $(".non-fiction").eq(1);

    var onButtonClick1 = function() {
    //Update current tab
      clickerButton1.addClass("current");
      clickerButton2.removeClass("current");
      clickerButton3.removeClass("current");

	  $shortArticles.show();
	  $bioArticles.hide();
	  $nonFicArticles.hide();
    }

    var onButtonClick2 = function() {
      clickerButton1.removeClass("current");
      clickerButton2.addClass("current");
      clickerButton3.removeClass("current");
      
	  $shortArticles.hide();
	  $bioArticles.show();
	  $nonFicArticles.hide();
	        
    }
    
    var onButtonClick3 = function () {
      clickerButton1.removeClass("current");
      clickerButton2.removeClass("current");
      clickerButton3.addClass("current"); 
      
      $shortArticles.hide();
	  $bioArticles.hide();
	  $nonFicArticles.show();    
    }*/

/*
    clickerButton1.on("click", onButtonClick1);
    clickerButton2.on("click", onButtonClick2);
    clickerButton3.on("click", onButtonClick3);*/
