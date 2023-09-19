package com.yun.jul212wc.main;


import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 1단계 : Map

public class WCMapper 
extends Mapper<Object, Text, Text, IntWritable>{
	private static final Text WORD = new Text();
	private static final IntWritable ONE = new IntWritable(1);
	// 한 문장 만날때 마다 불러짐
	@Override
	protected void map(
			Object key, // 데이터가 있나 검사하는 용도
			Text value, // 그 문장(I am a a boy.)
			Mapper<Object,Text,Text,IntWritable>.Context context) //결과처리 
			throws IOException ,InterruptedException {

		// split : 정형
		// StringTokenizer : 비정형

		String line = value.toString();	// Text -> String
		StringTokenizer st = new StringTokenizer(line, " ");
		
		while (st.hasMoreTokens()) {
			// String -> Text
			// int -> IntWritable
			WORD.set(st.nextToken());	// 값만 바꿔서 
			context.write(WORD, ONE);	// 다음단계로 결과 전송
		}
	} 
}


















