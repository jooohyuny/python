package com.yun.jul253kh.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class KHMain {
	public static void main(String[] args) {
		try {
			Job j = Job.getInstance(new Configuration());
			
			j.setMapperClass(KHMapper.class);
			j.setCombinerClass(KHReducer.class);
			j.setReducerClass(KHReducer.class);
			
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(IntWritable.class);
			
			FileInputFormat.addInputPath(j, new Path(args[0]));
			FileOutputFormat.setOutputPath(j, new Path(args[1]));
			
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
