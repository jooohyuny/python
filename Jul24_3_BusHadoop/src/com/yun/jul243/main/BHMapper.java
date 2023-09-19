package com.yun.jul243.main;

import java.io.IOException;
import java.text.SimpleDateFormat;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// in
//	2015,01,01,100번,시청앞,1000,5000

public class BHMapper extends Mapper<Object, Text, Text, LongWritable> {
	private static final SimpleDateFormat SDF = new SimpleDateFormat("yyyyMMdd");
	private static final SimpleDateFormat SDF2 = new SimpleDateFormat("E");
	
	private static final Text YOIL = new Text();
	private static final LongWritable SUM = new LongWritable();
	private static final LongWritable ONE = new LongWritable(1);
	
	@Override
	protected void map(
			Object key, 
			Text value, 
			Mapper<Object, Text, Text, LongWritable>.Context context)
			throws IOException, InterruptedException {
		try {
			String[] line = value.toString().split(",");
			String yoil = SDF2.format(SDF.parse(line[0]+line[1]+line[2]));
			
			YOIL.set(yoil + "_합");
			SUM.set(Long.parseLong(line[line.length-1])
					+ Long.parseLong(line[line.length-2]));
			context.write(YOIL, SUM);	// 월_합, 6000
			
			YOIL.set(yoil + "_데이터수");
			context.write(YOIL, ONE);	// 월_데이터수, 1
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
