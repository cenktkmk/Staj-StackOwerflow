

//!-- Code injected by live-server -->

    // <![CDATA[  <-- For SVG support
    if ('WebSocket' in window) {
        (function () {
            function refreshCSS() {
                var sheets = [].slice.call(document.getElementsByTagName("link"));
                var head = document.getElementsByTagName("head")[0];
                for (var i = 0; i < sheets.length; ++i) {
                    var elem = sheets[i];
                    var parent = elem.parentElement || head;
                    parent.removeChild(elem);
                    var rel = elem.rel;
                    if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
                        var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
                        elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
                    }
                    parent.appendChild(elem);
                }
            }
            var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
            var address = protocol + window.location.host + window.location.pathname + '/ws';
            var socket = new WebSocket(address);
            socket.onmessage = function (msg) {
                if (msg.data == 'reload') window.location.reload();
                else if (msg.data == 'refreshcss') refreshCSS();
            };
            if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
                console.log('Live reload enabled.');
                sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
            }
        })();
    }
    else {
        console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
    }
    // ]]>





    function changeText() {
        let textElement = document.getElementById("text");
        let originalText = textElement.innerText;
    
        // Toggle a CSS class to hide the element with a transition effect
        textElement.classList.add("hidden");
    
        // Wait for the transition to complete and then change the text to "New Text"
        setTimeout(function() {
            textElement.innerText = "developer";
            textElement.classList.remove("hidden");
        }, 2000);
    
        setTimeout(function() {
            // Toggle a CSS class to hide the element with a transition effect
            textElement.classList.add("hidden");
    
            // Wait for the transition to complete and then change the text to "New Text 2"
            setTimeout(function() {
                textElement.innerText = "data scientist";
                textElement.classList.remove("hidden");
            }, 2000);
        }, 4000); // Adjust the timing here to make it 2000ms after the first change
    
        // Set a timer to call the function again after a certain interval (e.g., 6 seconds)
        setTimeout(function() {
            // Toggle a CSS class to hide the element with a transition effect
            textElement.classList.add("hidden");
    
            // Wait for the transition to complete and then change the text to the original text
            setTimeout(function() {
                textElement.innerText = originalText;
                textElement.classList.remove("hidden");
            }, 2000);
    
            // Set a timer to call the function again after a certain interval (e.g., 6 seconds)
            setTimeout(changeText, 7000);
        }, 7000);
    }
    
    // Start the automatic text change
    changeText();
    
  

