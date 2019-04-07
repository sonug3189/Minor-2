var Twit = require('twit')
var fs = require('fs');

var T = new Twit({
  consumer_key:         'y5hMNDo85DDEz3NLPjqZi16EV',
  consumer_secret:      'fTl8t6I2D9jbNe3E3EhkPniWHQbPRRdoYNHIcdtu4DB8fd5Ra8',
  access_token:         '948604507906179072-ZC1saKov7svBH6M2zkJ9vMen84HALYY',
  access_token_secret:  'nVhQrhSCTlUQ6FPC3BNFWOMH0yEcQoi671Up7oLmZyi8s',
  timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
  strictSSL:            true,     // optional - requires SSL certificates to be valid.
})





function search_related_tweets(Word,count)
{
	T.get('search/tweets', { q: Word, count: count }, function(err, data, response) {
  console.log(data)
})
}


function search_followers(handle)
{
T.get('followers/ids', { screen_name: handle },  function (err, data, response) {
  console.log(data)
})
}


function post_status(text)
{
T.post('statuses/update', { status: text }, function(err, data, response) {
  console.log(data)
})
}


function repost_status(id)
{
T.post('statuses/retweet/:id', { id: '343360866131001345' }, function (err, data, response) {
  console.log(data)
})
 }
//
//  destroy a tweet with id '343360866131001345'
//
function delete_status(id)
{
	T.post('statuses/destroy/:id', { id: '343360866131001345' }, function (err, data, response) {
  console.log(data)
})

}

function post_image(filepath,alternateText,caption){
	var b64content = fs.readFileSync(filepath, { encoding: 'base64' })
    caption = caption + '#Rule no. ' + Math.floor(Math.random()*100); 
	T.post('media/upload', { media_data: b64content }, function (err, data, response) {
  	var mediaIdStr = data.media_id_string
  	var altText = alternateText
	  var meta_params = { media_id: mediaIdStr, alt_text: { text: altText } }
	 
	  T.post('media/metadata/create', meta_params, function (err, data, response) {
	    if (!err) {
		      // now we can reference the media and post a tweet (media will attach to the tweet)
	      var params = { status: caption, media_ids: [mediaIdStr] }
	 
	      T.post('statuses/update', params, function (err, data, response) {
	        console.log(data)
	      })
	    }
 	 })
	})
}


function dynamic_post_status(text)
{
	text = text + "   " + Math.floor(Math.random()*100) + "      #MajorProject"
T.post('statuses/update', { status: text }, function(err, data, response) {
  console.log(data)
})
}


 post_status("Rishav ka Project");
//post_image("C:/Users/Shaunak Chadha/Desktop/CAT/n.jpg","Truth of life","#Wednesday Calm and Active");
// search_related_tweets("California",100)
// search_followers('skywalker6197')

// dynamic_post_status("Arey bhai bhai bhai");
//setInterval(post_image , 1000*60*2)


