package com.example.wkpescherine.atawear;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ListView;
import android.widget.Toast;
import android.content.Intent;
import android.widget.ArrayAdapter;

import java.util.ArrayList;
import java.util.Set;

public class pairDevice extends AppCompatActivity {

    private static final int REQUEST_ENABLED = 0;
    private static final int REQUEST_DISCOVERABLE = 0;

    ListView list;
    BluetoothAdapter bluetoothAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_pair_device);

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if(bluetoothAdapter == null){
            Toast.makeText(this,"There is no bluetooth detected", Toast.LENGTH_SHORT).show();
            finish();
        }

    }

    public void turnOn(View v){
        Intent onIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
        startActivityForResult(onIntent, REQUEST_ENABLED);;
    }

    public void turnOff(View v){
        bluetoothAdapter.disable();
    }

    public void discoverable(View v){
        if(!bluetoothAdapter.isDiscovering()){
            Intent discoverable = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
            startActivityForResult(discoverable, REQUEST_DISCOVERABLE);;
        }

    }

    public void List(){
        Set<BluetoothDevice> paireddevices = bluetoothAdapter.getBondedDevices();

        ArrayList<String> devices = new ArrayList<String>();

        for(BluetoothDevice bt: paireddevices){
            devices.add(bt.getName());
        }

        ArrayAdapter arrayAdapter = new ArrayAdapter(pairDevice.this, android.R.layout.simple_list_item_1, devices);

        list.setAdapter(arrayAdapter);

    }
}
