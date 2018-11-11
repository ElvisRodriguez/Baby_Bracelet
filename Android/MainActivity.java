package com.example.wkpescherine.atawear;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Window;
import android.view.WindowManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);

    }

    public void toMonitor(View v){
        Intent toMonitor = new Intent(getApplicationContext(), ToMonitor.class);
        startActivity(toMonitor);
    }

    public void pairDevice(View v){
        Intent pairDevice = new Intent(getApplicationContext(), pairDevice.class);
        startActivity(pairDevice);
    }

    public void pairDevice2(View v){
        Intent pairDevice2 = new Intent(getApplicationContext(), pairDevice2.class);
        startActivity(pairDevice2);
    }

}
