package com.example.android_sp17.babybracletwebview;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = (WebView)findViewById(R.id.atawearwebview);
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("https://elvisrodriguez.pythonanywhere.com/");

        WebSettings webSettings = webView.getSettings(); //Enables settings on the Web.
        webSettings.setJavaScriptEnabled(true);

    }

    //This piece of code will prevent the app from going back to the home screen
    public void onBackPressed(){
        if (webView.canGoBack()){
            webView.goBack();;
        }
        else{
            super.onBackPressed();
        }
    }
}
