package com.yun.jul212wc.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

// 2단계 : Combine(자동으로 처리됨)
// IN
//		I 1
//		am 1
//		a 1
//		a 1
//		boy. 1
// OUT
//		I 1
//		am 1
//		a 1,1
//		boy. 1
///////////////////////////////////////
// 3단계 : Reduce
// IN
//		I 1
//		am 1
//		a 1,1
//		boy. 1
// OUT
//		I 1
//		am 1
//		a 2
//		boy. 1
public class WCReducer extends Reducer<Text, IntWritable, Text, IntWritable>{

	private static final IntWritable SUM = new IntWritable();
	
	@Override
	protected void reduce(
			Text arg0,	// a 
			Iterable<IntWritable> arg1,	// 1,1
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2)	// 결과처리 
			throws IOException, InterruptedException {
		
		int sum = 0;
		for(IntWritable iw : arg1) {
			sum += iw.get();
		}
		SUM.set(sum);
		arg2.write(arg0, SUM);	// a 2
	}
}



















