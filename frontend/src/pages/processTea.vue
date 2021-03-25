<template>
  <div id = "processTea">

    <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container>
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea  ></flowTea>
      </el-aside>
        <el-main>
          <div id="stu" >
<div id="block">
    <span class="demonstration">开题提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker :readonly="editable"
      v-model="value1"
      type="datetime"
      placeholder="选择日期时间"
      align="right">
    </el-date-picker>
</div>

<div id="block">
    <span class="demonstration">中期提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker :readonly="editable"
      v-model="value2"
      type="datetime"
      placeholder="选择日期时间"
      align="right"
      >
    </el-date-picker>

</div>
            <div id="block">
    <span class="demonstration">结题提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker :readonly="editable"
      v-model="value3"
      type="datetime"
      placeholder="选择日期时间"
      align="right"
      >
    </el-date-picker>
              <el-row>
              <el-button type="primary" v-show="editable" @click="editable = false">编辑</el-button>
      <el-button type="primary" v-show="!editable" @click="submitTime">确定</el-button>
                <el-tooltip placement="top-start">
  <div slot="content">请先在左侧设置每个阶段的截止日期，设置成功后可以通过下表查看每个同学的状态
    <br/>红色代表该同学未在截止时间内提交报告
  </div>
  <el-button style="float: right" type="info" icon="el-icon-question" circle></el-button>
</el-tooltip>
</el-row>
            </div>
            <el-divider><i class="el-icon-s-data"></i></el-divider>
    <el-table id="table"
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
      prop="number"
      label="学号"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="status"
      label="状态">
    </el-table-column>
  </el-table>
  </div>

        </el-main>
      </el-container>
    </el-container>
</div>
</template>

<style>

  #block{
    margin: 2% 10px;
  }
  #table{
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
    margin-top: 2%;
  }
  .el-roe-title{
    margin-bottom: 20px;
    
  }
  .el-col {
    border-radius: 4px;
  }
  .el-header-home{
    line-height: 40px;
    font-size: 20px;
  }
  .blog{
    background: #EEE ;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  .infinite-list-wrapper{
    height: 100vh;
  }
  .el-table .warning-row {
    background: oldlace;
  }
  #stu{
    margin:8px 10px;
  }

  .el-table .success-row {
    background: #f97880;
  }
</style>

<script>
import topNav from '../components/topNav'
import flowTea from '../components/flowTea'
  export default {
    name: 'home',
    components: {
      topNav,
      flowTea,
    },
    mounted() {
          this.getCurUserID();
      },
    methods: {
      tableRowClassName({row, rowIndex}) {
        for (var i = 0;i<this.rowarning.length;i++) {
          if (rowIndex == this.rowarning[i]) {
            return 'success-row';
          }
        }
        return '';
      },
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.getdata();
                  }
                  else{
                      this.$message.error("系统错误")
                    }
                })
      },
      getdata(){
        this.$http.post('/api/getTeacherProcess/',{'userId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.value1 = res1['time1'];
                      this.value2 = res1['time2'];
                      this.value3 = res1['time3'];
                      for (var i = 0;i<res1['stalist'].length;i++){
                        this.tableData.push({number:res1['stalist'][i][0],
                        name:res1['stalist'][i][1],
                        status:res1['stalist'][i][2]})
                        if(res1['stalist'][i][3] == 1){
                          this.rowarning.push(i)
                        }
                      }
                      console.log(this.rowarning);
                    }
                    else if(res1['err_code']==1){
                      this.$message.error("没有查询到流程信息，请先完成双选阶段")
                    }
                    else{
                      this.$message({
                      type: 'info',
                      message: '请完善各阶段时间'
                        });
                    }
              })
      },
      submitTime(){
        this.$http.post('/api/subTeacherProcess/',{'userId':this.watchId,'time1':String(this.value1),'time2':String(this.value2),'time3':String(this.value3)},{emulateJSON:true})
              .then(function(response){
                console.log(this.value1);
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '提交成功'
                        });
                      this.editable = true;
                    }
                    else{
                      this.$message.error("提交失败")
                    }
              })
      }

    },
    data() {
      return {
        tableData: [],
        watchId:'',
        role:'',
        editable:true,
        rowarning:[],
        pickerOptions: {
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '明天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() + 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周后',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        value1: '',
        value2: '',
        value3:'',
      }
    }
  }
</script>
