import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { presetPalettes } from "@ant-design/colors";
import { PageHeader } from "@ant-design/pro-layout";
import { Breadcrumb, Card, Col, Empty, Row, Space } from "antd";

import { formatDistanceToNow } from "date-fns";
import type { LatLngTuple, PointTuple } from "leaflet";
import { Doughnut } from "react-chartjs-2";
import { Popup } from "react-leaflet";

import type {
  GetDevicesSummaryResponse,
  GetGatewaysSummaryResponse,
} from "@chirpstack/chirpstack-api-grpc-web/api/internal_pb";
import {
  GetDevicesSummaryRequest,
  GetGatewaysSummaryRequest,
} from "@chirpstack/chirpstack-api-grpc-web/api/internal_pb";

import type { GatewayListItem, ListGatewaysResponse } from "@chirpstack/chirpstack-api-grpc-web/api/gateway_pb";
import { GatewayState, ListGatewaysRequest } from "@chirpstack/chirpstack-api-grpc-web/api/gateway_pb";

import { ArcElement, Chart as ChartJS, Legend, Tooltip } from "chart.js";
import type { MarkerColor } from "../../components/Map";
import Map, { Marker } from "../../components/Map";
import GatewayStore from "../../stores/GatewayStore";
import InternalStore from "../../stores/InternalStore";
import { useTitle } from "../helpers";

ChartJS.register(ArcElement, Tooltip, Legend);
ChartJS.defaults.font.family = "Consolas";
ChartJS.defaults.plugins.tooltip.titleFont = { weight: "bold", size: 13 };
ChartJS.defaults.plugins.tooltip.mode = "index";
ChartJS.defaults.plugins.legend.labels.font = { weight: "bold" };
ChartJS.defaults.animation = false;
ChartJS.defaults.plugins.legend.display = false;
ChartJS.defaults.plugins.legend.position = "bottom";
ChartJS.defaults.plugins.legend.labels.font = {
  size: 14,
  weight: 600,
};

function GatewaysMap() {
  const [items, setItems] = useState<GatewayListItem[]>([]);

  useEffect(() => {
    const req = new ListGatewaysRequest();
    req.setLimit(9999);
    GatewayStore.list(req, (resp: ListGatewaysResponse) => {
      setItems(resp.getResultList());
    });
  }, []);

  if (items.length === 0) {
    return <Empty />;
  }

  const boundsOptions: {
    padding: PointTuple;
  } = {
    padding: [50, 50],
  };

  const bounds: LatLngTuple[] = [];
  const markers: JSX.Element[] = [];

  for (const item of items) {
    const pos: LatLngTuple = [item.getLocation()!.getLatitude(), item.getLocation()!.getLongitude()];
    bounds.push(pos);

    let color: MarkerColor = "orange";
    let lastSeen: string = "Never seen online";

    if (item.getState() === GatewayState.OFFLINE) {
      color = "red";
    } else if (item.getState() === GatewayState.ONLINE) {
      color = "green";
    }

    if (item.getLastSeenAt() !== undefined) {
      lastSeen = formatDistanceToNow(item.getLastSeenAt()!.toDate(), { addSuffix: true });
    }

    markers.push(
      <Marker position={[pos[0], pos[1]]} faIcon="wifi" color={color}>
        <Popup>
          <Link to={`/tenants/${item.getTenantId()}/gateways/${item.getGatewayId()}`}>{item.getName()}</Link>
          <br />
          {item.getGatewayId()}
          <br />
          <br />
          {lastSeen}
        </Popup>
      </Marker>,
    );
  }

  return (
    <Map height={500} bounds={bounds} boundsOptions={boundsOptions}>
      {markers}
    </Map>
  );
}

function DevicesActiveInactive({ summary }: { summary?: GetDevicesSummaryResponse }) {
  if (
    summary === undefined ||
    (summary.getNeverSeenCount() === 0 && summary.getInactiveCount() === 0 && summary.getActiveCount() === 0)
  ) {
    return <Empty />;
  }

  const data = {
    labels: ["Never seen", "Inactive", "Active"],
    datasets: [
      {
        cutout: "75%",
        data: [summary.getNeverSeenCount(), summary.getInactiveCount(), summary.getActiveCount()],
        backgroundColor: [presetPalettes.orange.primary, presetPalettes.red.primary, presetPalettes.green.primary],
      },
    ],
  };

  const options: {
    animation: boolean;
    responsive: boolean;
    maintainAspectRatio: boolean;
  } = {
    animation: false,
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div className="chart-doughnut">
      <Doughnut data={data} options={options} />
      <div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "gray",
                marginRight: "8px",
              }}></span>
            <span>Never Seen</span>
          </div>
          <strong>{summary.getNeverSeenCount()}</strong>
        </div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "red",
                marginRight: "8px",
              }}></span>
            <span>Offline</span>
          </div>
          <strong>{summary.getInactiveCount()}</strong>
        </div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "green",
                marginRight: "8px",
              }}></span>
            <span>Online</span>
          </div>
          <strong>{summary.getActiveCount()}</strong>
        </div>
      </div>
    </div>
  );
}

function GatewaysActiveInactive({ summary }: { summary?: GetGatewaysSummaryResponse }) {
  if (
    summary === undefined ||
    (summary.getNeverSeenCount() === 0 && summary.getOfflineCount() === 0 && summary.getOnlineCount() === 0)
  ) {
    return <Empty />;
  }

  const data = {
    labels: ["Never seen", "Offline", "Online"],
    datasets: [
      {
        cutout: "75%",
        data: [summary.getNeverSeenCount(), summary.getOfflineCount(), summary.getOnlineCount()],
        backgroundColor: [presetPalettes.orange.primary, presetPalettes.red.primary, presetPalettes.green.primary],
      },
    ],
  };

  const options: {
    animation: boolean;
    responsive: boolean;
    maintainAspectRatio: boolean;
  } = {
    animation: false,
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div className="chart-doughnut">
      <Doughnut data={data} options={options} />
      <div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "gray",
                marginRight: "8px",
              }}></span>
            <span>Never Seen</span>
          </div>
          <strong>{summary.getNeverSeenCount()}</strong>
        </div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "red",
                marginRight: "8px",
              }}></span>
            <span>Offline</span>
          </div>
          <strong>{summary.getOfflineCount()}</strong>
        </div>
        <div className="chart-legends">
          <div>
            <span
              style={{
                display: "inline-block",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "green",
                marginRight: "8px",
              }}></span>
            <span>Online</span>
          </div>
          <strong>{summary.getOnlineCount()}</strong>
        </div>
      </div>
    </div>
  );
}

function DevicesDataRates({ summary }: { summary?: GetDevicesSummaryResponse }) {
  const getColor = (dr: number) => {
    return [
      "#ff5722",
      "#ff9800",
      "#ffc107",
      "#ffeb3b",
      "#cddc39",
      "#8bc34a",
      "#4caf50",
      "#009688",
      "#00bcd4",
      "#03a9f4",
      "#2196f3",
      "#3f51b5",
      "#673ab7",
      "#9c27b0",
      "#e91e63",
    ][dr];
  };

  if (summary === undefined || summary.getDrCountMap().toArray().length === 0) {
    return <Empty />;
  }

  const data: {
    labels: string[];
    datasets: {
      cutout: string;
      data: number[];
      backgroundColor: string[];
    }[];
  } = {
    labels: [],
    datasets: [
      {
        cutout: "75%",
        data: [],
        backgroundColor: [],
      },
    ],
  };

  for (const elm of summary.getDrCountMap().toArray()) {
    data.labels.push(`DR${elm[0]}`);
    data.datasets[0].data.push(elm[1]);
    data.datasets[0].backgroundColor.push(getColor(elm[0]));
  }
  const drMapArray = summary.getDrCountMap().toArray();
  const options: {
    animation: boolean;
    responsive: boolean;
    maintainAspectRatio: boolean;
  } = {
    animation: false,
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div className="chart-doughnut">
      <Doughnut data={data} options={options} />
      <div>
        {drMapArray.map((elm, idx) => (
          <div
            key={idx}
            className="chart-legends"
            style={{ display: "flex", alignItems: "center", marginBottom: "4px" }}>
            <div>
              <span
                style={{
                  display: "inline-block",
                  width: "12px",
                  height: "12px",
                  borderRadius: "50%",
                  backgroundColor: getColor(elm[0]),
                  marginRight: "8px",
                }}></span>
              <span>{`DR${elm[0]}`}</span>
            </div>
            <strong style={{ marginLeft: "6px" }}>{elm[1]}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}

function Dashboard() {
  useTitle("Network Server", "Dashboard");
  const [gatewaysSummary, setGatewaysSummary] = useState<GetGatewaysSummaryResponse | undefined>(undefined);
  const [devicesSummary, setDevicesSummary] = useState<GetDevicesSummaryResponse | undefined>(undefined);

  useEffect(() => {
    InternalStore.getGatewaysSummary(new GetGatewaysSummaryRequest(), (resp: GetGatewaysSummaryResponse) => {
      setGatewaysSummary(resp);
    });

    InternalStore.getDevicesSummary(new GetDevicesSummaryRequest(), (resp: GetDevicesSummaryResponse) => {
      setDevicesSummary(resp);
    });
  }, []);

  return (
    <Space direction="vertical" style={{ width: "100%" }} size="large">
      <PageHeader
        breadcrumbRender={() => (
          <Breadcrumb>
            <Breadcrumb.Item>
              <span>Network Server</span>
            </Breadcrumb.Item>
            <Breadcrumb.Item>
              <span>Dashboard</span>
            </Breadcrumb.Item>
          </Breadcrumb>
        )}
        title="Dashboard"
      />
      <Row gutter={24}>
        <Col span={8} className="rotiot-card-header">
          <Card title="Active devices">
            <DevicesActiveInactive summary={devicesSummary} />
          </Card>
        </Col>
        <Col span={8} className="rotiot-card-header">
          <Card title="Active gateways">
            <GatewaysActiveInactive summary={gatewaysSummary} />
          </Card>
        </Col>
        <Col span={8} className="rotiot-card-header">
          <Card title="Device data-rate usage">
            <DevicesDataRates summary={devicesSummary} />
          </Card>
        </Col>
      </Row>
      <Card title="Gateway map">
        <GatewaysMap />
      </Card>
    </Space>
  );
}

export default Dashboard;
