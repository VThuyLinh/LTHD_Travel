import { ScrollView, TouchableOpacity, View } from "react-native"
import MyStyle from "../../styles/MyStyle"
import { ActivityIndicator, Button, Card, Chip, Text } from "react-native-paper"
import React from "react"
import APIs, { endpoints } from "../../configs/APIs"
import moment from "moment"

import Icon from "react-native-vector-icons/FontAwesome6"

const News =({navigation}) =>
    {
        const [news,setNews]=React.useState([]);

        const loadNews = async () =>{
            try{
                let res= await APIs.get(endpoints['news']);
                setNews(res.data);
            }
            catch (ex){
                console.error(ex);
                
            }
        }

        React.useEffect(()=>{
             loadNews();
            },[]);
        return(
        <View style={MyStyle.container}>
            
            <ScrollView>
            {news === null ? <ActivityIndicator/>:<>
                {news.map(c=> 
                <Card mode="elevated" style={MyStyle.card} >
                    <Card.Content>
                    <Text style={MyStyle.text1}>{c.Name_News}</Text>
                    </Card.Content>
                    <Card.Cover source={{ uri:`${c.image_thumbnail}`.replace("https://tlinh.pythonanywhere.com/news/","https://tlinh.pythonanywhere.com/static/news/") }} />
                    <Text style={MyStyle.text2}>Ngày đăng: {moment(c.DatePost).fromNow()}</Text>
                   
                    <Card.Actions>
                    <TouchableOpacity onPress={()=>navigation.navigate("newsdetail",{'news_id':c.id})} key={c.id}><Text style={MyStyle.icon}><Icon color="#153050" size={20} name="mountain-sun"></Icon>  Xem thêm</Text></TouchableOpacity>
                    </Card.Actions>
                </Card>)}
            </>}   
            </ScrollView>
        </View>
        
        );
    }

export default News;